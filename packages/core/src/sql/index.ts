import { AsyncLocalStorage } from "node:async_hooks";
import * as DrizzleSchema from "@foodtools/core/src/sql/schema";
import type { AwsDataApiPgDatabase } from "drizzle-orm/aws-data-api/pg";
import type { NodePgDatabase } from "drizzle-orm/node-postgres";

export type DBType =
	| AwsDataApiPgDatabase<typeof DrizzleSchema>
	| NodePgDatabase<typeof DrizzleSchema>;

type DbContext = {
	db: DBType;
};
const dbContext = new AsyncLocalStorage<DbContext>();

export const runInDbContext = (db: DBType, fn: () => unknown) => {
	return dbContext.run({ db }, fn);
};

let _client: DBType;

const getDb = (): DBType => {
	if (_client) return _client;

	// Local development uses TCP connection via DATABASE_URL
	if (process.env.DATABASE_URL) {
		const { drizzle } = require("drizzle-orm/node-postgres") as typeof import("drizzle-orm/node-postgres");
		const { Pool } = require("pg") as typeof import("pg");
		const pool = new Pool({
			connectionString: process.env.DATABASE_URL,
			max: 100,
		});
		_client = drizzle(pool, { schema: DrizzleSchema });
		return _client;
	}

	// AWS uses RDS Data API
	const { drizzle } = require("drizzle-orm/aws-data-api/pg") as typeof import("drizzle-orm/aws-data-api/pg");
	const { RDSDataClient } = require("@aws-sdk/client-rds-data") as typeof import("@aws-sdk/client-rds-data");
	const { Resource } = require("sst") as { Resource: Record<string, unknown> };

	// Type assertion needed until SST generates types for the Database resource
	const db = Resource.Database as {
		database: string;
		secretArn: string;
		clusterArn: string;
	};

	_client = drizzle(new RDSDataClient({}), {
		database: db.database,
		secretArn: db.secretArn,
		resourceArn: db.clusterArn,
		schema: DrizzleSchema,
	});

	return _client;
};

export type DBTransaction = Parameters<Parameters<DBType["transaction"]>[0]>[0];

export { getDb, DrizzleSchema as schema };
