import { Resource } from "sst";

export type SecretName = "BETTER_AUTH_SECRET" | "RESEND_API_KEY";

const getSecret = (name: SecretName): string => {
	const envValue = process.env[name];
	if (envValue) return envValue;
	// In the template, fall back to placeholder values.
	switch (name) {
		case "BETTER_AUTH_SECRET":
			return Resource.BETTER_AUTH_SECRET.value;
		case "RESEND_API_KEY":
			return Resource.RESEND_API_KEY.value;
	}
};

export { getSecret };
