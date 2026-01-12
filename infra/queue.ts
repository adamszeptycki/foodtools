import { documentsBucket } from "./storage";
import { dbUrl, openAiApiKey } from "./config";

// Queue for processing uploaded documents in the background
export const documentProcessingQueue = new sst.aws.Queue("DocumentProcessingQueue", {
	handler: "packages/core/src/workers/document-processor.handler",
	timeout: "10 minutes",
	link: [documentsBucket, dbUrl, openAiApiKey],
	transform: {
		handler: {
			environment: {
				DOCUMENTS_BUCKET_NAME: documentsBucket.name,
			},
		},
	},
});
