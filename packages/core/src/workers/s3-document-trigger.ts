import type { S3Handler } from "aws-lambda";
import { getDocumentByS3Key } from "../sql/queries/service-documents/queries";
import { processDocument } from "./document-processor";

/**
 * S3 event handler - triggered when a file is uploaded to the documents bucket
 * Looks up the document record by S3 key and triggers processing
 */
export const handler: S3Handler = async (event) => {
	for (const record of event.Records) {
		const s3Key = decodeURIComponent(record.s3.object.key.replace(/\+/g, " "));

		console.log(`S3 event received for key: ${s3Key}`);

		// Look up the document by S3 key
		const doc = await getDocumentByS3Key(s3Key);

		if (!doc) {
			console.log(`No document record found for S3 key: ${s3Key}, skipping`);
			continue;
		}

		console.log(`Found document ${doc.id} for S3 key: ${s3Key}`);

		// Process the document
		await processDocument(doc.id);
	}
};
