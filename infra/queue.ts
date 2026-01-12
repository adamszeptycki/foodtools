import { dbUrl, openAiApiKey } from "./config";
import { documentsBucket } from "./storage";

export const documentProcessingQueueDlq = new sst.aws.Queue("DocumentProcessingQueueDLQ");
export const documentProcessingQueue = new sst.aws.Queue("DocumentProcessingQueue", {
	visibilityTimeout: "5 minutes",
	dlq: documentProcessingQueueDlq.arn,
});

documentProcessingQueue.subscribe({
	handler: "packages/core/src/workers/document-processor.handler",
	timeout: "5 minutes",
	link: [documentsBucket, dbUrl, openAiApiKey],
});