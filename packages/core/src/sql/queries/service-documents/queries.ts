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

/**
 * Search for fixes using dual embedding similarity
 * Matches against BOTH original and summarized embeddings using OR logic
 * Returns the best similarity score from either embedding
 */
export async function searchFixesByDualSimilarity(
	userId: string,
	queryEmbedding: number[],
	limit: number = 10,
	minSimilarity: number = 0.5,
) {
	const db = getDb();
	const embeddingStr = JSON.stringify(queryEmbedding);

	// Use GREATEST to get the best similarity from either embedding
	// COALESCE handles null embeddings (for records that don't have summarized embeddings yet)
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
			similarity: sql<number>`GREATEST(
				COALESCE(1 - (${machineFixes.embedding} <=> ${embeddingStr}::vector), 0),
				COALESCE(1 - (${machineFixes.embeddingSummarized} <=> ${embeddingStr}::vector), 0)
			)`,
			originalSimilarity: sql<number>`COALESCE(1 - (${machineFixes.embedding} <=> ${embeddingStr}::vector), 0)`,
			summarizedSimilarity: sql<number>`COALESCE(1 - (${machineFixes.embeddingSummarized} <=> ${embeddingStr}::vector), 0)`,
		})
		.from(machineFixes)
		.where(
			sql`${machineFixes.userId} = ${userId} AND GREATEST(
				COALESCE(1 - (${machineFixes.embedding} <=> ${embeddingStr}::vector), 0),
				COALESCE(1 - (${machineFixes.embeddingSummarized} <=> ${embeddingStr}::vector), 0)
			) > ${minSimilarity}`,
		)
		.orderBy(
			sql`GREATEST(
				COALESCE(1 - (${machineFixes.embedding} <=> ${embeddingStr}::vector), 0),
				COALESCE(1 - (${machineFixes.embeddingSummarized} <=> ${embeddingStr}::vector), 0)
			) DESC`,
		)
		.limit(limit);

	return results;
}

/**
 * Search for fixes using PostgreSQL full-text search (BM25-style ranking)
 * Uses ts_rank with normalization option 32 for document length normalization
 */
export async function searchFixesByFullText(
	userId: string,
	query: string,
	limit: number = 10,
) {
	const db = getDb();

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
			rank: sql<number>`ts_rank(${machineFixes.searchVector}, plainto_tsquery('english', ${query}), 32)`,
		})
		.from(machineFixes)
		.where(
			sql`${machineFixes.userId} = ${userId}
				AND ${machineFixes.searchVector} IS NOT NULL
				AND ${machineFixes.searchVector} @@ plainto_tsquery('english', ${query})`,
		)
		.orderBy(
			sql`ts_rank(${machineFixes.searchVector}, plainto_tsquery('english', ${query}), 32) DESC`,
		)
		.limit(limit);

	return results;
}

/**
 * Hybrid search combining embedding similarity and full-text search
 * Uses Reciprocal Rank Fusion (RRF) to combine rankings
 *
 * @param embeddingWeight - Weight for embedding results (default 0.6)
 * @param textWeight - Weight for full-text results (default 0.4)
 * @param k - RRF constant (default 60, higher values give more weight to lower ranks)
 */
export async function searchFixesHybrid(
	userId: string,
	queryEmbedding: number[],
	queryText: string,
	limit: number = 10,
	embeddingWeight: number = 0.6,
	textWeight: number = 0.4,
) {
	const db = getDb();
	const embeddingStr = JSON.stringify(queryEmbedding);
	const k = 60; // RRF constant

	// Combined query using RRF scoring
	// RRF score = sum(weight / (k + rank)) for each ranking source
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
			embeddingSimilarity: sql<number>`GREATEST(
				COALESCE(1 - (${machineFixes.embedding} <=> ${embeddingStr}::vector), 0),
				COALESCE(1 - (${machineFixes.embeddingSummarized} <=> ${embeddingStr}::vector), 0)
			)`,
			textRank: sql<number>`COALESCE(
				ts_rank(${machineFixes.searchVector}, plainto_tsquery('english', ${queryText}), 32),
				0
			)`,
			// Combined RRF-style score using normalized ranks
			rrfScore: sql<number>`(
				${embeddingWeight} * GREATEST(
					COALESCE(1 - (${machineFixes.embedding} <=> ${embeddingStr}::vector), 0),
					COALESCE(1 - (${machineFixes.embeddingSummarized} <=> ${embeddingStr}::vector), 0)
				) +
				${textWeight} * COALESCE(
					ts_rank(${machineFixes.searchVector}, plainto_tsquery('english', ${queryText}), 32),
					0
				)
			)`,
		})
		.from(machineFixes)
		.where(sql`${machineFixes.userId} = ${userId}`)
		.orderBy(
			sql`(
				${embeddingWeight} * GREATEST(
					COALESCE(1 - (${machineFixes.embedding} <=> ${embeddingStr}::vector), 0),
					COALESCE(1 - (${machineFixes.embeddingSummarized} <=> ${embeddingStr}::vector), 0)
				) +
				${textWeight} * COALESCE(
					ts_rank(${machineFixes.searchVector}, plainto_tsquery('english', ${queryText}), 32),
					0
				)
			) DESC`,
		)
		.limit(limit);

	return results;
}
