import { GetObjectCommand, PutObjectCommand, S3Client } from "@aws-sdk/client-s3";
import { SendMessageCommand, SQSClient } from "@aws-sdk/client-sqs";
import { getSignedUrl } from "@aws-sdk/s3-request-presigner";
import type { Context } from "@foodtools/core-web/src/trpc/context";
import { TRPCError } from "@trpc/server";
import { Resource } from "sst";

// Helpers to safely access SST Resources with fallbacks for build time
function getBucketName() {
	try {
		return Resource.ServiceDocumentsBucket.name;
	} catch {
		return process.env.DOCUMENTS_BUCKET_NAME || "service-documents-bucket";
	}
}

function getQueueUrl() {
	try {
		const url = Resource.DocumentProcessingQueue.url;
		console.log("Queue URL from Resource:", url);
		return url;
	} catch (e) {
		console.log("Failed to get queue URL from Resource:", e);
		const fallback = process.env.QUEUE_URL || "";
		console.log("Using fallback queue URL:", fallback);
		if (!fallback) {
			throw new Error("Queue URL not available - DocumentProcessingQueue not linked");
		}
		return fallback;
	}
}

import { generateEmbeddings } from "@foodtools/core/src/domain/ai/generate-embeddings";
import {
	createServiceDocument,
	deleteDocument as deleteDocumentMutation,
} from "@foodtools/core/src/sql/queries/service-documents/mutations";
import {
	getDocumentById,
	getDocumentStatusCounts,
	getDocumentWithFixes,
	listAllFixes,
	listDocumentsByUser,
	searchFixesBySimilarity,
	searchFixesBySubstring,
	searchFixesByDualSimilarity,
	searchFixesByFullText,
} from "@foodtools/core/src/sql/queries/service-documents/queries";

type ProtectedContext = Context & {
	session: { user: NonNullable<Context["session"]>["user"] };
};

const s3 = new S3Client({});
const sqs = new SQSClient({});

/**
 * Initiate document upload - generates S3 presigned URL and creates DB record
 */
export async function initiateUpload(
	ctx: ProtectedContext,
	input: { fileName: string; fileSize: number; mimeType: string },
) {
	const userId = ctx.session.user.id;

	// Generate unique S3 key
	const timestamp = Date.now();
	const randomStr = Math.random().toString(36).substring(7);
	const s3Key = `documents/${userId}/${timestamp}-${randomStr}-${input.fileName}`;

	const bucketName = getBucketName();

	// Generate presigned URL for direct browser upload
	const command = new PutObjectCommand({
		Bucket: bucketName,
		Key: s3Key,
		ContentType: input.mimeType,
		ContentLength: input.fileSize,
	});

	const uploadUrl = await getSignedUrl(s3, command, { expiresIn: 3600 }); // 1 hour

	// Create document record in database
	const document = await createServiceDocument({
		userId,
		fileName: input.fileName,
		fileSize: input.fileSize,
		s3Key,
		s3Bucket: bucketName,
		mimeType: input.mimeType,
		processingStatus: "pending",
	});

	return {
		documentId: document.id,
		uploadUrl,
		s3Key,
	};
}

/**
 * Initiate batch document upload - generates multiple S3 presigned URLs and creates DB records
 */
export async function initiateUploadBatch(
	ctx: ProtectedContext,
	input: { files: Array<{ fileName: string; fileSize: number; mimeType: string }> },
) {
	const userId = ctx.session.user.id;
	const bucketName = getBucketName();

	// Process all files in parallel
	const results = await Promise.all(
		input.files.map(async (file) => {
			// Generate unique S3 key
			const timestamp = Date.now();
			const randomStr = Math.random().toString(36).substring(7);
			const s3Key = `documents/${userId}/${timestamp}-${randomStr}-${file.fileName}`;

			// Generate presigned URL for direct browser upload
			const command = new PutObjectCommand({
				Bucket: bucketName,
				Key: s3Key,
				ContentType: file.mimeType,
				ContentLength: file.fileSize,
			});

			const uploadUrl = await getSignedUrl(s3, command, { expiresIn: 3600 }); // 1 hour

			// Create document record in database
			const document = await createServiceDocument({
				userId,
				fileName: file.fileName,
				fileSize: file.fileSize,
				s3Key,
				s3Bucket: bucketName,
				mimeType: file.mimeType,
				processingStatus: "pending",
			});

			return {
				fileName: file.fileName,
				documentId: document.id,
				uploadUrl,
				s3Key,
			};
		}),
	);

	return results;
}

type ProcessingStatus = "pending" | "processing" | "completed" | "failed";

/**
 * List all documents for the current user with pagination and optional status filter
 */
export async function listDocuments(
	ctx: ProtectedContext,
	input: { limit?: number; offset?: number; status?: ProcessingStatus },
) {
	const userId = ctx.session.user.id;
	return listDocumentsByUser(userId, {
		limit: input.limit ?? 10,
		offset: input.offset ?? 0,
		status: input.status,
	});
}

/**
 * Get document counts by status for the current user
 */
export async function getStatusCounts(ctx: ProtectedContext) {
	const userId = ctx.session.user.id;
	return getDocumentStatusCounts(userId);
}

/**
 * Get a specific document with its fixes
 */
export async function getDocument(
	ctx: ProtectedContext,
	input: { id: string },
) {
	const userId = ctx.session.user.id;
	const doc = await getDocumentWithFixes(input.id);

	if (!doc || doc.userId !== userId) {
		throw new TRPCError({
			code: "NOT_FOUND",
			message: "Document not found",
		});
	}

	return doc;
}

/**
 * Delete a document and all associated fixes
 */
export async function deleteDocument(
	ctx: ProtectedContext,
	input: { id: string },
) {
	const userId = ctx.session.user.id;
	const doc = await getDocumentById(input.id);

	if (!doc || doc.userId !== userId) {
		throw new TRPCError({
			code: "NOT_FOUND",
			message: "Document not found",
		});
	}

	// Note: In production, consider deleting from S3 as well
	// await s3.send(new DeleteObjectCommand({
	//   Bucket: doc.s3Bucket,
	//   Key: doc.s3Key,
	// }));

	// Delete from database (cascade will delete fixes)
	await deleteDocumentMutation(input.id);

	return { success: true };
}

/**
 * List all fixes for the current user
 */
export async function listFixes(
	ctx: ProtectedContext,
	input: { limit?: number; machineType?: string },
) {
	const userId = ctx.session.user.id;
	return listAllFixes(userId, input.limit, input.machineType);
}

/**
 * Semantic search for similar fixes using multiple search strategies:
 * 1. Substring matching (ILIKE) - highest priority for exact matches
 * 2. Dual embedding search (original + summarized) - semantic similarity
 * 3. BM25 full-text search - keyword matching with ranking
 *
 * Results are combined and deduplicated, with scoring metadata included
 */
export async function semanticSearch(
	ctx: ProtectedContext,
	input: { query: string; limit: number; minSimilarity: number },
) {
	const userId = ctx.session.user.id;

	// Generate embedding for semantic search (needed for steps 2 and 3)
	const queryEmbedding = await generateEmbeddings(input.query);

	// Run all three search strategies in parallel
	const [substringResults, dualEmbeddingResults, fullTextResults] = await Promise.all([
		// 1. Substring search (exact ILIKE matches) - highest priority
		searchFixesBySubstring(userId, input.query, input.limit),

		// 2. Dual embedding search (original + summarized embeddings)
		searchFixesByDualSimilarity(userId, queryEmbedding, input.limit, 0.5),

		// 3. BM25 full-text search
		searchFixesByFullText(userId, input.query, input.limit),
	]);

	// Track seen IDs for deduplication
	const seenIds = new Set<string>();
	const combined: Array<{
		id: string;
		documentId: string;
		machineModel: string | null;
		machineType: string | null;
		problemDescription: string;
		solutionApplied: string;
		partsUsed: string | null;
		labourHours: number | null;
		clientName: string | null;
		serviceDate: Date | null;
		createdAt: Date;
		similarity: number;
		matchType: "substring" | "embedding" | "fulltext";
	}> = [];

	// Add substring matches first (similarity = 1.0, highest priority)
	for (const result of substringResults) {
		if (!seenIds.has(result.id)) {
			seenIds.add(result.id);
			combined.push({
				...result,
				similarity: 1.0,
				matchType: "substring",
			});
		}
	}

	// Add dual embedding results (use best similarity from either embedding)
	for (const result of dualEmbeddingResults) {
		if (!seenIds.has(result.id)) {
			seenIds.add(result.id);
			combined.push({
				id: result.id,
				documentId: result.documentId,
				machineModel: result.machineModel,
				machineType: result.machineType,
				problemDescription: result.problemDescription,
				solutionApplied: result.solutionApplied,
				partsUsed: result.partsUsed,
				labourHours: result.labourHours,
				clientName: result.clientName,
				serviceDate: result.serviceDate,
				createdAt: result.createdAt,
				similarity: result.similarity,
				matchType: "embedding",
			});
		}
	}

	// Add full-text results (normalize rank to 0-1 range, with cap at 0.9)
	for (const result of fullTextResults) {
		if (!seenIds.has(result.id)) {
			seenIds.add(result.id);
			// ts_rank typically returns values between 0 and 1, but can exceed 1
			// Normalize and cap at 0.9 to prioritize embedding matches
			const normalizedRank = Math.min(result.rank, 0.9);
			combined.push({
				...result,
				similarity: normalizedRank,
				matchType: "fulltext",
			});
		}
	}

	// Sort by similarity (descending) and return top results
	combined.sort((a, b) => b.similarity - a.similarity);

	return combined.slice(0, input.limit);
}

/**
 * Reprocess an existing document without re-uploading
 * Sends message to SQS queue for background processing
 */
export async function reprocessDocument(
	ctx: ProtectedContext,
	input: { documentId: string },
) {
	const userId = ctx.session.user.id;
	const doc = await getDocumentById(input.documentId);

	if (!doc || doc.userId !== userId) {
		throw new TRPCError({
			code: "NOT_FOUND",
			message: "Document not found",
		});
	}

	// Send message to SQS queue to start processing
	const queueUrl = getQueueUrl();

	await sqs.send(
		new SendMessageCommand({
			QueueUrl: queueUrl,
			MessageBody: JSON.stringify({
				documentId: doc.id,
			}),
		}),
	);

	return { success: true };
}

/**
 * Get a presigned URL for viewing/downloading a document PDF
 */
export async function getDocumentUrl(
	ctx: ProtectedContext,
	input: { documentId: string },
) {
	const userId = ctx.session.user.id;
	const doc = await getDocumentById(input.documentId);

	if (!doc || doc.userId !== userId) {
		throw new TRPCError({
			code: "NOT_FOUND",
			message: "Document not found",
		});
	}

	const command = new GetObjectCommand({
		Bucket: doc.s3Bucket,
		Key: doc.s3Key,
		ResponseContentDisposition: `inline; filename="${doc.fileName}"`,
		ResponseContentType: "application/pdf",
	});

	const url = await getSignedUrl(s3, command, { expiresIn: 3600 }); // 1 hour

	return { url };
}
