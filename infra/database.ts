import { vpc } from "./vpc";
import { Stage } from "./stages";

// Local development database configuration
const localDevConfig = {
	host: "localhost",
	port: 5937,
	username: "postgres",
	password: "postgres",
	database: "foodtools",
};

export const database = (() => {
	// Production gets its own cluster, always-on
	if ($app.stage === Stage.PROD) {
		return new sst.aws.Aurora("Database", {
			engine: "postgres",
			vpc,
			dataApi: true,
			scaling: {
				min: "0.5 ACU", // Always-on for prod
				max: "4 ACU",
			},
		});
	}

	// DEV stage creates the shared Aurora cluster with auto-pause
	if ($app.stage === Stage.DEV) {
		return new sst.aws.Aurora("Database", {
			engine: "postgres",
			vpc,
			dataApi: true,
			scaling: {
				min: "0 ACU",
				max: "4 ACU",
				pauseAfter: "5 minutes",
			},
			dev: localDevConfig,
		});
	}

	// Developer stages (adam, justme, etc.) use local postgres
	return new sst.aws.Aurora("Database", {
		engine: "postgres",
		vpc,
		dataApi: true,
		scaling: {
			min: "0 ACU",
			max: "4 ACU",
			pauseAfter: "5 minutes",
		},
		dev: localDevConfig,
	});
})();
