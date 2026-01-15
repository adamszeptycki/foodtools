import { GetObjectCommand, S3Client } from "@aws-sdk/client-s3";
import { extractStructuredData } from "@foodtools/core/src/domain/ai/extract-structured-data";
import { generateEmbeddings } from "@foodtools/core/src/domain/ai/generate-embeddings";
import { extractTextFromPDF } from "@foodtools/core/src/domain/pdf/extract-text";
import { getDb } from "@foodtools/core/src/sql";
import { getDocumentByS3KeyAndBucket } from "@foodtools/core/src/sql/queries/service-documents/queries";
import {
	machineFixes,
	serviceDocuments,
} from "@foodtools/core/src/sql/schema";
import type { S3Event, SQSHandler } from "aws-lambda";
import { eq } from "drizzle-orm";

const s3 = new S3Client({});

/**
 * Convert a Readable stream to a Buffer
 */
async function streamToBuffer(stream: any): Promise<Buffer> {
	const chunks: Uint8Array[] = [];
	for await (const chunk of stream) {
		chunks.push(chunk);
	}
	return Buffer.concat(chunks);
}

/**
 * Core document processing logic - can be called from SQS or S3 handlers
 */
export async function processDocument(documentId: string): Promise<void> {
	const db = getDb();

	try {
		console.log(`Processing document ${documentId}`);

		// Step 1: Delete any existing fixes (for reprocessing)
		const deletedFixes = await db
			.delete(machineFixes)
			.where(eq(machineFixes.documentId, documentId))
			.returning();
		if (deletedFixes.length > 0) {
			console.log(`Deleted ${deletedFixes.length} existing fixes`);
		}

		// Step 2: Mark document as processing
		await db
			.update(serviceDocuments)
			.set({ processingStatus: "processing", processingError: null })
			.where(eq(serviceDocuments.id, documentId));

		// Step 3: Get document record from database
		const [doc] = await db
			.select()
			.from(serviceDocuments)
			.where(eq(serviceDocuments.id, documentId));

		if (!doc) {
			throw new Error(`Document ${documentId} not found in database`);
		}

		console.log(`Found document: ${doc.fileName} (S3: ${doc.s3Key})`);

		// Step 4: Download PDF from S3
		const s3Response = await s3.send(
			new GetObjectCommand({
				Bucket: doc.s3Bucket,
				Key: doc.s3Key,
			}),
		);

		if (!s3Response.Body) {
			throw new Error("No body in S3 response");
		}

		const pdfBuffer = await streamToBuffer(s3Response.Body);
		console.log(`Downloaded PDF (${pdfBuffer.length} bytes)`);

		// Step 5: Extract text from PDF
		const extractedText = await extractTextFromPDF(pdfBuffer);
		console.log(`Extracted ${extractedText.length} characters of text`);

		// Step 6: Update document with extracted text
		await db
			.update(serviceDocuments)
			.set({
				extractedText,
				textLength: extractedText.length,
			})
			.where(eq(serviceDocuments.id, documentId));

		// Step 7: Extract structured data using OpenAI
		const fixes = await extractStructuredData(extractedText);
		console.log(`Extracted ${fixes.length} fix record(s)`);

		// Step 8: Generate embeddings and store each fix
		for (const fix of fixes) {
			// Create searchable text from fix data for embedding
			const searchableText = `
${fix.problemDescription}
      `.trim();

			console.log(`Generating embeddings for fix: ${fix.problemDescription.substring(0, 50)}...`);

			// Generate embedding
			const embedding = await generateEmbeddings(searchableText);

			// Store fix with embedding in database
			await db.insert(machineFixes).values({
				documentId: doc.id,
				userId: doc.userId,
				// Client Info
				clientName: fix.clientName,
				clientAddress: fix.clientAddress,
				clientPhone: fix.clientPhone,
				// Equipment Info
				machineModel: fix.machineModel,
				machineType: fix.machineType,
				serialNumber: fix.serialNumber,
				// Service Details
				problemDescription: fix.problemDescription,
				solutionApplied: fix.solutionApplied,
				partsUsed: fix.partsUsed,
				serviceDate: fix.serviceDate ? new Date(fix.serviceDate) : null,
				// Technician Info
				technicianName: fix.technicianName,
				technicianId: fix.technicianId,
				// Labour
				labourHours: fix.labourHours,
				// Embedding
				embedding,
				embeddingModel: "text-embedding-3-small",
			});

			console.log(`Stored fix in database with embedding`);
		}

		// Step 9: Mark document as completed
		await db
			.update(serviceDocuments)
			.set({
				processingStatus: "completed",
				processedAt: new Date(),
			})
			.where(eq(serviceDocuments.id, documentId));

		console.log(`Successfully processed document ${documentId}`);
	} catch (error) {
		console.error(`Error processing document ${documentId}:`, error);

		// Mark document as failed with error message
		await db
			.update(serviceDocuments)
			.set({
				processingStatus: "failed",
				processingError:
					error instanceof Error ? error.message : "Unknown error",
			})
			.where(eq(serviceDocuments.id, documentId));

		throw error;
	}
}

/**
 * SQS handler for processing uploaded service documents
 * Used for manual reprocessing via the reprocess button
 */
export const handler: SQSHandler = async (event) => {
	console.log("SQS Handler invoked with", event.Records.length, "records");

	for (const record of event.Records) {
		const s3Event: S3Event & { Event?: string } = JSON.parse(record.body);
		// Skip test events
		if (s3Event.Event === "s3:TestEvent") {
			console.log("Skipping S3 test event");
			continue;
		}
		for (const record of s3Event.Records) {
			const s3Key = record.s3.object.key;
			const s3BucketName = record.s3.bucket.name;

			const document = await getDocumentByS3KeyAndBucket(s3Key, s3BucketName);
			console.log(`Found document ${document.id} for S3 key: ${s3Key}`);
			await processDocument(document.id);
		}
	}

	console.log("SQS Handler completed");
};
