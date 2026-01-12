import { dbUrl, openAiApiKey } from "./config";

// S3 bucket for storing uploaded PDF service documents
export const documentsBucket = new sst.aws.Bucket("ServiceDocumentsBucket", {
	access: "private",
	transform: {
		bucket: {
			cors: [{
				allowedHeaders: ["*"],
				allowedMethods: ["GET", "PUT", "POST"],
				allowedOrigins: ["*"], // TODO: Restrict in production to actual domain
				maxAgeSeconds: 3000,
			}],
		},
	},
});

// Subscribe to S3 object creation events to trigger document processing
documentsBucket.subscribe({
	handler: "packages/core/src/workers/s3-document-trigger.handler",
	timeout: "30 seconds",
	link: [dbUrl, openAiApiKey, documentsBucket],
	filterPrefix: "documents/",
}, {
	events: ["s3:ObjectCreated:*"],
});
