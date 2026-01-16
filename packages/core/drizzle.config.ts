import type { Config } from "drizzle-kit";
import { defineConfig } from "drizzle-kit";

const config: Config = {
	dialect: "postgresql",
	schema: "./src/sql/schema/*",
	out: "./src/sql/migrations/",
	dbCredentials: {
		url: process.env.DATABASE_URL || "postgres://postgres:postgres@localhost:5937/foodtools",
	},
	// Print all statements
	// verbose: true,
	// Always ask for confirmation
	strict: true,
};

export default defineConfig(config);
