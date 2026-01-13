import { betterAuthSecret, dbUrl, openAiApiKey, resendApiKey } from "./config";
import { documentProcessingQueue } from "./queue";
import { getDomain, router } from "./router";
import { documentsBucket } from "./storage";

export const nextJsPage = new sst.aws.Nextjs("FoodToolsWeb", {
	link: [betterAuthSecret, dbUrl, resendApiKey, openAiApiKey, documentsBucket, documentProcessingQueue],
	path: "packages/web",
	route: $app.stage === "prod" ? { router } : undefined,
	warm: 1,
	server: {
		timeout: "1 minute",
	},
	environment: {
		BETTER_AUTH_SECRET: process.env.BETTER_AUTH_SECRET,
		BETTER_AUTH_URL: getDomain({ protocol: "https", skipLocalhost: false }),
		NEXT_PUBLIC_BASE_URL: getDomain({ protocol: "https", skipLocalhost: false }),
	},
});
