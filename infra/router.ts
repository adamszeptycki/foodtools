
const baseUrl = "foodtools.jetbridge.click"
export function getDomain({
	protocol,
	skipLocalhost,
}: { protocol?: string; skipLocalhost?: boolean }): string {
	let result: string;
	switch ($app.stage) {
		case "adam":
		case "justme":
			if (skipLocalhost) {
				result = baseUrl;
			} else {
				result = "https://localhost:3000"
			}
			break
		case "prod":
			result = baseUrl;
			break;
		default:
			result = skipLocalhost ? baseUrl : "https://localhost:3000";
	}
	if (protocol && !result.startsWith("http")) {
		result = `${protocol}://${result}`;
	}
	return result;
}

const domain = getDomain({ skipLocalhost: true });
const isProd = $app.stage === "production"
export const router = new sst.aws.Router("FoodToolsRouter", {
	domain: isProd ? {
		name: domain,
			aliases: [`*.${domain}`],
		}
		: undefined,
});


