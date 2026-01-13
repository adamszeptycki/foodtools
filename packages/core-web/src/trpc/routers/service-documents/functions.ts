import { S3Client, PutObjectCommand } from "@aws-sdk/client-s3";
import { SQSClient, SendMessageCommand } from "@aws-sdk/client-sqs";
import { getSignedUrl } from "@aws-sdk/s3-request-presigner";
import { Resource } from "sst";
import type { Context } from "@foodtools/core-web/src/trpc/context";
import { TRPCError } from "@trpc/server";

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
import {
	createServiceDocument,
	deleteDocument as deleteDocumentMutation,
} from "@foodtools/core/src/sql/queries/service-documents/mutations";
import {
	getDocumentById,
	listDocumentsByUser,
	getDocumentWithFixes,
	listAllFixes,
	searchFixesBySimilarity,
} from "@foodtools/core/src/sql/queries/service-documents/queries";
import { generateEmbeddings } from "@foodtools/core/src/domain/ai/generate-embeddings";

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
 * Confirm upload and trigger background processing
 */
export async function confirmUpload(
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
 * List all documents for the current user
 */
export async function listDocuments(
	ctx: ProtectedContext,
	input: { limit?: number; offset?: number },
) {
	const userId = ctx.session.user.id;
	return listDocumentsByUser(userId);
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
 * Semantic search for similar fixes using vector embeddings
 */
export async function semanticSearch(
	ctx: ProtectedContext,
	input: { query: string; limit: number; minSimilarity: number },
) {
	const userId = ctx.session.user.id;

	// Generate embedding for the search query
	const queryEmbedding = await generateEmbeddings(input.query);

	// Search for similar fixes using pgvector
	const results = await searchFixesBySimilarity(
		userId,
		queryEmbedding,
		input.limit,
		0.5,
		// input.minSimilarity ,
	);

	return results;
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
