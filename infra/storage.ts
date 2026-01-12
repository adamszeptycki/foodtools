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
