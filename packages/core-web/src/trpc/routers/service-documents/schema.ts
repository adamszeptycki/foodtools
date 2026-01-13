import { z } from "zod";

export const getDocumentSchema = z.object({
	id: z.string().uuid(),
});

export const deleteDocumentSchema = z.object({
	id: z.string().uuid(),
});

export const listDocumentsSchema = z.object({
	limit: z.number().optional(),
	offset: z.number().optional(),
});

export const semanticSearchSchema = z.object({
	query: z.string().min(1).max(1000),
	limit: z.number().min(1).max(50).default(10),
	minSimilarity: z.number().min(0).max(1).default(0.7),
});

export const listFixesSchema = z.object({
	limit: z.number().optional(),
	machineType: z.string().optional(),
});

export const getFixSchema = z.object({
	id: z.string().uuid(),
});

export const initiateUploadSchema = z.object({
	fileName: z.string().min(1).max(255),
	fileSize: z.number().positive().max(10 * 1024 * 1024), // Max 10MB
	mimeType: z.string().regex(/^application\/pdf$/),
});

export const confirmUploadSchema = z.object({
	documentId: z.string().uuid(),
});

export const reprocessDocumentSchema = z.object({
	documentId: z.string().uuid(),
});

export const getDocumentUrlSchema = z.object({
	documentId: z.string().uuid(),
});
