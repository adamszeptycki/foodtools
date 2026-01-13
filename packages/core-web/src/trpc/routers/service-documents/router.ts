import { protectedProcedure, router } from "@foodtools/core-web/src/trpc/trpc";
import {
	initiateUpload,
	initiateUploadBatch,
	confirmUpload,
	listDocuments,
	getDocument,
	deleteDocument,
	listFixes,
	semanticSearch,
	reprocessDocument,
	getDocumentUrl,
} from "./functions";
import {
	initiateUploadSchema,
	initiateUploadBatchSchema,
	confirmUploadSchema,
	listDocumentsSchema,
	getDocumentSchema,
	deleteDocumentSchema,
	listFixesSchema,
	semanticSearchSchema,
	reprocessDocumentSchema,
	getDocumentUrlSchema,
} from "./schema";

export const serviceDocumentsRouter = router({
	/**
	 * Initiate document upload
	 * Returns presigned S3 URL for direct browser upload
	 */
	initiateUpload: protectedProcedure
		.input(initiateUploadSchema)
		.mutation(async ({ ctx, input }) => {
			return initiateUpload(ctx, input);
		}),

	/**
	 * Initiate batch document upload
	 * Returns presigned S3 URLs for multiple files in a single request
	 */
	initiateUploadBatch: protectedProcedure
		.input(initiateUploadBatchSchema)
		.mutation(async ({ ctx, input }) => {
			return initiateUploadBatch(ctx, input);
		}),

	/**
	 * Confirm upload completion and trigger background processing
	 */
	confirmUpload: protectedProcedure
		.input(confirmUploadSchema)
		.mutation(async ({ ctx, input }) => {
			return confirmUpload(ctx, input);
		}),

	/**
	 * List all documents for current user
	 */
	list: protectedProcedure
		.input(listDocumentsSchema.optional())
		.query(async ({ ctx, input }) => {
			return listDocuments(ctx, input || {});
		}),

	/**
	 * Get a specific document with its fixes
	 */
	get: protectedProcedure
		.input(getDocumentSchema)
		.query(async ({ ctx, input }) => {
			return getDocument(ctx, input);
		}),

	/**
	 * Delete a document and all associated fixes
	 */
	delete: protectedProcedure
		.input(deleteDocumentSchema)
		.mutation(async ({ ctx, input }) => {
			return deleteDocument(ctx, input);
		}),

	/**
	 * List all extracted fixes
	 */
	listFixes: protectedProcedure
		.input(listFixesSchema.optional())
		.query(async ({ ctx, input }) => {
			return listFixes(ctx, input || {});
		}),

	/**
	 * Semantic search for similar fixes using vector similarity
	 */
	semanticSearch: protectedProcedure
		.input(semanticSearchSchema)
		.mutation(async ({ ctx, input }) => {
			return semanticSearch(ctx, input);
		}),

	/**
	 * Reprocess an existing document without re-uploading
	 */
	reprocess: protectedProcedure
		.input(reprocessDocumentSchema)
		.mutation(async ({ ctx, input }) => {
			return reprocessDocument(ctx, input);
		}),

	/**
	 * Get presigned URL for viewing/downloading a document PDF
	 */
	getDocumentUrl: protectedProcedure
		.input(getDocumentUrlSchema)
		.query(async ({ ctx, input }) => {
			return getDocumentUrl(ctx, input);
		}),
});
