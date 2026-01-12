import { getDb } from "@foodtools/core/src/sql";
import {
	serviceDocuments,
	type InsertServiceDocument,
} from "@foodtools/core/src/sql/schema";
import { eq } from "drizzle-orm";

/**
 * Create a new service document record
 */
export async function createServiceDocument(data: InsertServiceDocument) {
	const db = getDb();
	const [doc] = await db
		.insert(serviceDocuments)
		.values(data)
		.returning();
	return doc;
}

/**
 * Update the processing status of a document
 */
export async function updateDocumentStatus(
	id: string,
	status: "pending" | "processing" | "completed" | "failed",
	error?: string,
) {
	const db = getDb();
	const [doc] = await db
		.update(serviceDocuments)
		.set({
			processingStatus: status,
			processingError: error,
			processedAt: status === "completed" ? new Date() : undefined,
		})
		.where(eq(serviceDocuments.id, id))
		.returning();
	return doc;
}

/**
 * Delete a service document (cascade deletes fixes)
 */
export async function deleteDocument(id: string) {
	const db = getDb();
	const [deleted] = await db
		.delete(serviceDocuments)
		.where(eq(serviceDocuments.id, id))
		.returning();
	return deleted;
}
