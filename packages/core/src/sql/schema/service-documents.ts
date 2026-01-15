import { defaultFields } from "@foodtools/core/src/sql/utils";
import {
	customType,
	index,
	integer,
	pgEnum,
	pgTable,
	real,
	text,
	timestamp,
	uuid,
} from "drizzle-orm/pg-core";
import { createInsertSchema, createSelectSchema } from "drizzle-zod";
import { users } from "./auth";

// Custom vector type for pgvector
export const vector = customType<{
	data: number[];
	driverData: string;
	config: { dimensions: number };
}>({
	dataType(config) {
		return `vector(${config?.dimensions ?? 1536})`;
	},
	fromDriver(value: string): number[] {
		// pgvector returns vectors as strings like '[1,2,3]'
		return JSON.parse(value);
	},
	toDriver(value: number[]): string {
		// Convert array to pgvector format
		return JSON.stringify(value);
	},
});

// Processing status enum
export const processingStatusEnum = pgEnum("processing_status", [
	"pending",
	"processing",
	"completed",
	"failed",
]);

// Service documents table
export const serviceDocuments = pgTable(
	"service_documents",
	{
		...defaultFields,
		userId: uuid("user_id")
			.notNull()
			.references(() => users.id, { onDelete: "cascade" }),
		fileName: text("file_name").notNull(),
		fileSize: integer("file_size").notNull(), // in bytes
		s3Key: text("s3_key").notNull().unique(),
		s3Bucket: text("s3_bucket").notNull(),
		mimeType: text("mime_type").notNull(),
		processingStatus: processingStatusEnum("processing_status")
			.notNull()
			.default("pending"),
		processingError: text("processing_error"),
		processedAt: timestamp("processed_at"),
		extractedText: text("extracted_text"),
		textLength: integer("text_length"),
	},
	(table) => ({
		userIdIdx: index("service_documents_user_id_idx").on(table.userId),
		statusIdx: index("service_documents_status_idx").on(table.processingStatus),
	}),
);

// Infer types
export type ServiceDocument = typeof serviceDocuments.$inferSelect;
export type InsertServiceDocument = typeof serviceDocuments.$inferInsert;

// Zod schemas
export const ServiceDocumentSchema = createSelectSchema(serviceDocuments);
export const InsertServiceDocumentSchema = createInsertSchema(
	serviceDocuments,
).omit({
	id: true,
	createdAt: true,
	updatedAt: true,
});

// Machine fixes table
export const machineFixes = pgTable(
	"machine_fixes",
	{
		...defaultFields,
		documentId: uuid("document_id")
			.notNull()
			.references(() => serviceDocuments.id, { onDelete: "cascade" }),
		userId: uuid("user_id")
			.notNull()
			.references(() => users.id, { onDelete: "cascade" }),

		// Client Info
		clientName: text("client_name"),
		clientAddress: text("client_address"),
		clientPhone: text("client_phone"),

		// Equipment Info
		machineModel: text("machine_model"),
		machineType: text("machine_type"),
		serialNumber: text("serial_number"),

		// Service Details
		problemDescription: text("problem_description").notNull(),
		solutionApplied: text("solution_applied").notNull(),
		partsUsed: text("parts_used"),
		serviceDate: timestamp("service_date"),

		// Technician Info
		technicianName: text("technician_name"),
		technicianId: text("technician_id"),

		// Labour
		labourHours: real("labour_hours"),

		// Embedding and search
		embedding: vector("embedding", { dimensions: 1536 }),
		embeddingModel: text("embedding_model").default("text-embedding-3-small"),

		// Metadata
		extractionConfidence: integer("extraction_confidence"),
		notes: text("notes"),
	},
	(table) => ({
		documentIdIdx: index("machine_fixes_document_id_idx").on(table.documentId),
		userIdIdx: index("machine_fixes_user_id_idx").on(table.userId),
		machineTypeIdx: index("machine_fixes_machine_type_idx").on(
			table.machineType,
		),
		// Vector similarity index using HNSW (pgvector)
		// Note: This index needs to be created manually in migration using CREATE INDEX
		// embeddingIdx: index("machine_fixes_embedding_idx").using("hnsw", table.embedding.op("vector_cosine_ops")),
	}),
);

// Infer types
export type MachineFix = typeof machineFixes.$inferSelect;
export type InsertMachineFix = typeof machineFixes.$inferInsert;

// Zod schemas
export const MachineFixSchema = createSelectSchema(machineFixes);
export const InsertMachineFixSchema = createInsertSchema(machineFixes).omit({
	id: true,
	createdAt: true,
	updatedAt: true,
});
