/**
 * Backfill Script: Dual Embeddings and Full-Text Search
 *
 * This script updates existing machine_fixes records with:
 * 1. summarizedSearchableText - LLM-generated summary of problem description
 * 2. embeddingSummarized - Embedding of the summarized text
 * 3. searchVector - Full-text search vector (tsvector)
 *
 * Usage:
 *   sst shell -- npx tsx packages/core/src/scripts/backfill-embeddings.ts
 *
 * Options:
 *   --dry-run     Preview changes without applying them
 *   --batch-size  Number of records per batch (default: 10)
 *   --delay       Delay between API calls in ms (default: 200)
 */

import { getDb } from "@foodtools/core/src/sql";
import { machineFixes } from "@foodtools/core/src/sql/schema";
import { generateEmbeddings } from "@foodtools/core/src/domain/ai/generate-embeddings";
import { summarizeProblemDescription } from "@foodtools/core/src/domain/ai/summarize-problem";
import { eq, isNull, sql, or, and } from "drizzle-orm";

// Parse command line arguments
const args = process.argv.slice(2);
const isDryRun = args.includes("--dry-run");
const batchSizeArg = args.find((a) => a.startsWith("--batch-size="));
const delayArg = args.find((a) => a.startsWith("--delay="));

const BATCH_SIZE = batchSizeArg ? parseInt(batchSizeArg.split("=")[1], 10) : 10;
const API_DELAY_MS = delayArg ? parseInt(delayArg.split("=")[1], 10) : 200;

// Helper to delay between API calls
const delay = (ms: number) => new Promise((resolve) => setTimeout(resolve, ms));

async function backfillEmbeddings() {
	const db = getDb();

	console.log("=".repeat(60));
	console.log("Backfill Script: Dual Embeddings and Full-Text Search");
	console.log("=".repeat(60));
	console.log(`Mode: ${isDryRun ? "DRY RUN (no changes will be made)" : "LIVE"}`);
	console.log(`Batch size: ${BATCH_SIZE}`);
	console.log(`API delay: ${API_DELAY_MS}ms`);
	console.log("=".repeat(60));

	// Find records that need backfilling
	// Records are candidates if they have a problemDescription but are missing
	// either summarizedSearchableText, embeddingSummarized, or searchVector
	const recordsToUpdate = await db
		.select({
			id: machineFixes.id,
			problemDescription: machineFixes.problemDescription,
			solutionApplied: machineFixes.solutionApplied,
			machineModel: machineFixes.machineModel,
			machineType: machineFixes.machineType,
			clientName: machineFixes.clientName,
			partsUsed: machineFixes.partsUsed,
			serialNumber: machineFixes.serialNumber,
			searchableText: machineFixes.searchableText,
			summarizedSearchableText: machineFixes.summarizedSearchableText,
		})
		.from(machineFixes)
		.where(
			or(
				isNull(machineFixes.summarizedSearchableText),
				isNull(machineFixes.embeddingSummarized),
				isNull(machineFixes.searchVector),
			),
		);

	console.log(`Found ${recordsToUpdate.length} records to backfill\n`);

	if (recordsToUpdate.length === 0) {
		console.log("Nothing to do. All records are up to date.");
		return;
	}

	if (isDryRun) {
		console.log("DRY RUN: Would update the following records:");
		for (const record of recordsToUpdate.slice(0, 5)) {
			console.log(`  - ${record.id}: "${record.problemDescription.substring(0, 50)}..."`);
		}
		if (recordsToUpdate.length > 5) {
			console.log(`  ... and ${recordsToUpdate.length - 5} more`);
		}
		return;
	}

	let processed = 0;
	let errors = 0;

	for (const record of recordsToUpdate) {
		try {
			console.log(`[${processed + 1}/${recordsToUpdate.length}] Processing ${record.id}...`);

			// Set searchable text if not already set
			const searchableText = record.searchableText || record.problemDescription.trim();

			// Generate summary if not already set
			let summarizedSearchableText = record.summarizedSearchableText;
			if (!summarizedSearchableText) {
				console.log("  Generating summary...");
				summarizedSearchableText = await summarizeProblemDescription(searchableText);
				await delay(API_DELAY_MS);
			}

			// Generate embedding for summarized text
			console.log("  Generating embedding for summary...");
			const embeddingSummarized = await generateEmbeddings(summarizedSearchableText);
			await delay(API_DELAY_MS);

			// Build full-text search content
			const fullTextSearchContent = [
				record.problemDescription,
				record.solutionApplied,
				record.machineModel,
				record.machineType,
				record.clientName,
				record.partsUsed,
				record.serialNumber,
			]
				.filter(Boolean)
				.join(" ");

			// Update the record
			console.log("  Updating database...");
			await db
				.update(machineFixes)
				.set({
					searchableText,
					summarizedSearchableText,
					embeddingSummarized,
					searchVector: sql`to_tsvector('english', ${fullTextSearchContent})`,
				})
				.where(eq(machineFixes.id, record.id));

			processed++;
			console.log(`  Done! (${processed}/${recordsToUpdate.length})\n`);
		} catch (error) {
			errors++;
			console.error(`  ERROR processing ${record.id}:`, error);
			console.log("  Continuing with next record...\n");
		}
	}

	console.log("=".repeat(60));
	console.log("Backfill Complete!");
	console.log(`  Processed: ${processed}`);
	console.log(`  Errors: ${errors}`);
	console.log(`  Total: ${recordsToUpdate.length}`);
	console.log("=".repeat(60));
}

// Run the script
backfillEmbeddings()
	.then(() => {
		console.log("\nScript finished successfully.");
		process.exit(0);
	})
	.catch((error) => {
		console.error("\nScript failed with error:", error);
		process.exit(1);
	});
