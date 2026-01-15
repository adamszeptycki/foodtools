import { dbUrl, openAiApiKey } from "./config";
import { documentsBucket } from "./storage";

const MAX_RESERVED_CONCURENCY_FOR_SQS_TASK = 2;

export const documentProcessingQueueDlq = new sst.aws.Queue("DocumentProcessingQueueDLQ");
export const documentProcessingQueue = new sst.aws.Queue("DocumentProcessingQueue", {
	visibilityTimeout: "5 minutes",
	dlq: documentProcessingQueueDlq.arn,
});

documentProcessingQueue.subscribe({
	handler: "packages/core/src/workers/document-processor.handler",
	timeout: "5 minutes",
	link: [documentsBucket, dbUrl, openAiApiKey],

	concurrency: {
		reserved: MAX_RESERVED_CONCURENCY_FOR_SQS_TASK,
	},
}, {
	batch: {size:1},
});


documentsBucket.notify({
	notifications: [
		{
			name: "S3BucketQueueSubscriber",
			queue: documentProcessingQueue,
			events: ["s3:ObjectCreated:*"]
		}
	]
});

