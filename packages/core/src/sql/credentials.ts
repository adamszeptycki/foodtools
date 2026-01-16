type DatabaseCredentials = {
	databaseUrl: string;
};

const getDatabaseCredentials = (): DatabaseCredentials => {
	const url = process.env.DATABASE_URL;
	if (!url) {
		throw new Error("DATABASE_URL not set for local development");
	}
	return { databaseUrl: url };
};

export { getDatabaseCredentials };
