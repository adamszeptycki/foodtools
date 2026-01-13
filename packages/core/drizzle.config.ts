import { getDatabaseCredentials } from "@foodtools/core/src/sql/credentials";
import type { Config } from "drizzle-kit";
import { defineConfig } from "drizzle-kit";

const dbCredentials = getDatabaseCredentials();

const config: Config = {
	dialect: "postgresql",
	schema: "./src/sql/schema/*",
	out: "./src/sql/migrations/",
	dbCredentials: {
		url: dbCredentials.databaseUrl,
	},
	// Print all statements
	// verbose: true,
	// Always ask for confirmation
	strict: true,
};

export default defineConfig(config);
