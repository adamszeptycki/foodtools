import { getDb } from "@foodtools/core/src/sql";
import {
	serviceDocuments,
	machineFixes,
} from "@foodtools/core/src/sql/schema";
import { eq, desc, sql, and } from "drizzle-orm";

/**
 * Get a service document by ID
 */
export async function getDocumentById(id: string) {
	const db = getDb();
	const [doc] = await db
		.select()
		.from(serviceDocuments)
		.where(eq(serviceDocuments.id, id));
	return doc;
}

/**
 * Get a service document by S3 key
 */
export async function getDocumentByS3Key(s3Key: string) {
	const db = getDb();
	const [doc] = await db
		.select()
		.from(serviceDocuments)
		.where(eq(serviceDocuments.s3Key, s3Key));
	return doc;
}

/**
 * List all documents for a specific user
 */
export async function listDocumentsByUser(userId: string) {
	const db = getDb();
	return db
		.select()
		.from(serviceDocuments)
		.where(eq(serviceDocuments.userId, userId))
		.orderBy(desc(serviceDocuments.createdAt));
}

/**
 * Get a document with all its associated fixes
 */
export async function getDocumentWithFixes(documentId: string) {
	const db = getDb();

	const doc = await getDocumentById(documentId);
	if (!doc) return null;

	const fixes = await db
		.select()
		.from(machineFixes)
		.where(eq(machineFixes.documentId, documentId))
		.orderBy(desc(machineFixes.createdAt));

	return { ...doc, fixes };
}

/**
 * List all fixes for a user, optionally filtered by machine type
 */
export async function listAllFixes(
	userId: string,
	limit?: number,
	machineType?: string,
) {
	const db = getDb();

	// Build where conditions
	const whereConditions = machineType
		? and(eq(machineFixes.userId, userId), eq(machineFixes.machineType, machineType))
		: eq(machineFixes.userId, userId);

	// Build and execute query with optional limit
	const baseQuery = db
		.select()
		.from(machineFixes)
		.where(whereConditions)
		.orderBy(desc(machineFixes.createdAt));

	if (limit) {
		return baseQuery.limit(limit);
	}

	return baseQuery;
}

/**
 * Search for fixes by semantic similarity using pgvector
 * Uses cosine distance to find most similar embeddings
 */
export async function searchFixesBySimilarity(
	userId: string,
	queryEmbedding: number[],
	limit: number = 10,
	minSimilarity: number = 0.7,
) {
	const db = getDb();

	// Convert embedding array to string format for pgvector
	const embeddingStr = JSON.stringify(queryEmbedding);

	// Use pgvector cosine similarity operator
	// 1 - (embedding <=> query) gives cosine similarity (0 to 1)
	// We filter for similarity > minSimilarity and order by distance (ascending)
	const results = await db
		.select({
			id: machineFixes.id,
			documentId: machineFixes.documentId,
			machineModel: machineFixes.machineModel,
			machineType: machineFixes.machineType,
			problemDescription: machineFixes.problemDescription,
			solutionApplied: machineFixes.solutionApplied,
			partsUsed: machineFixes.partsUsed,
			clientName: machineFixes.clientName,
			serviceDate: machineFixes.serviceDate,
			createdAt: machineFixes.createdAt,
			similarity: sql<number>`1 - (${machineFixes.embedding} <=> ${embeddingStr}::vector)`,
		})
		.from(machineFixes)
		.where(
			sql`${machineFixes.userId} = ${userId} AND 1 - (${machineFixes.embedding} <=> ${embeddingStr}::vector) > ${minSimilarity}`,
		)
		.orderBy(sql`${machineFixes.embedding} <=> ${embeddingStr}::vector`)
		.limit(limit);

	return results;
}

/**
 * Search for fixes by substring match using ILIKE
 * Searches across clientName, machineModel, machineType, serialNumber, problemDescription
 */
export async function searchFixesBySubstring(
	userId: string,
	query: string,
	limit: number = 10,
) {
	const db = getDb();
	const pattern = `%${query}%`;

	const results = await db
		.select({
			id: machineFixes.id,
			documentId: machineFixes.documentId,
			machineModel: machineFixes.machineModel,
			machineType: machineFixes.machineType,
			problemDescription: machineFixes.problemDescription,
			solutionApplied: machineFixes.solutionApplied,
			partsUsed: machineFixes.partsUsed,
			clientName: machineFixes.clientName,
			serviceDate: machineFixes.serviceDate,
			createdAt: machineFixes.createdAt,
		})
		.from(machineFixes)
		.where(
			sql`${machineFixes.userId} = ${userId} AND (
				${machineFixes.clientName} ILIKE ${pattern} OR
				${machineFixes.machineModel} ILIKE ${pattern} OR
				${machineFixes.machineType} ILIKE ${pattern} OR
				${machineFixes.serialNumber} ILIKE ${pattern} OR
				${machineFixes.problemDescription} ILIKE ${pattern}
			)`,
		)
		.limit(limit);

	return results;
}
