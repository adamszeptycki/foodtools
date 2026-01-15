

export const getBucketName = (_bucket: never): string => {
	throw new Error("No buckets defined in the foodtools template.");
};

export type QueueUrls = 
	| "OcrQueue"
	| "EmbeddingsQueue"
	| "S3BucketQueue"
	| "SmallTaskQueue"
	| "DocumentExtraction"
	| "EvalQueue"

export const getResourceUrl = (_resource: QueueUrls): string => {
	throw new Error("No external resources defined in the foodtools template.");
};
