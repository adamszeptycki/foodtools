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
 * Get a service document by S3 key and bucket name
 */
export async function getDocumentByS3KeyAndBucket(s3Key: string, s3Bucket: string) {
	const db = getDb();
	const [doc] = await db
		.select()
		.from(serviceDocuments)
		.where(
			and(
				eq(serviceDocuments.s3Key, s3Key),
				eq(serviceDocuments.s3Bucket, s3Bucket)
			)
		);
	return doc;
}

type ProcessingStatus = "pending" | "processing" | "completed" | "failed";

/**
 * List documents for a specific user with pagination and optional status filter
 */
export async function listDocumentsByUser(
	userId: string,
	options: { limit?: number; offset?: number; status?: ProcessingStatus } = {},
) {
	const db = getDb();
	const { limit = 10, offset = 0, status } = options;

	const whereCondition = status
		? and(
				eq(serviceDocuments.userId, userId),
				eq(serviceDocuments.processingStatus, status),
			)
		: eq(serviceDocuments.userId, userId);

	const [documents, countResult] = await Promise.all([
		db
			.select()
			.from(serviceDocuments)
			.where(whereCondition)
			.orderBy(desc(serviceDocuments.createdAt))
			.limit(limit)
			.offset(offset),
		db
			.select({ count: sql<number>`count(*)::int` })
			.from(serviceDocuments)
			.where(whereCondition),
	]);

	return {
		documents,
		total: countResult[0]?.count ?? 0,
	};
}

/**
 * Get document counts grouped by processing status for a user
 */
export async function getDocumentStatusCounts(userId: string) {
	const db = getDb();

	const result = await db
		.select({
			status: serviceDocuments.processingStatus,
			count: sql<number>`count(*)::int`,
		})
		.from(serviceDocuments)
		.where(eq(serviceDocuments.userId, userId))
		.groupBy(serviceDocuments.processingStatus);

	const counts = {
		all: 0,
		pending: 0,
		processing: 0,
		completed: 0,
		failed: 0,
	};

	for (const row of result) {
		counts[row.status as keyof typeof counts] = row.count;
		counts.all += row.count;
	}

	return counts;
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
			labourHours: machineFixes.labourHours,
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
			labourHours: machineFixes.labourHours,
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
