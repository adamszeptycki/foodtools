import OpenAI from "openai";
import { Resource } from "sst";

// Helper to get OpenAI API key with fallback for build time
function getOpenAIKey() {
	try {
		return Resource.OPENAI_API_KEY.value;
	} catch {
		return process.env.OPENAI_API_KEY || "";
	}
}

const openai = new OpenAI({
	apiKey: getOpenAIKey(),
});

/**
 * Generate vector embeddings for text using OpenAI's text-embedding-3-small model
 * @param text - Text to generate embeddings for
 * @returns Array of 1536 floating point numbers representing the embedding
 */
export async function generateEmbeddings(text: string): Promise<number[]> {
	try {
		const response = await openai.embeddings.create({
			model: "text-embedding-3-small", // 1536 dimensions, cost-effective
			input: text,
			encoding_format: "float",
		});

		return response.data[0].embedding;
	} catch (error) {
		console.error("Error generating embeddings:", error);
		throw new Error(
			`Failed to generate embeddings: ${error instanceof Error ? error.message : "Unknown error"}`,
		);
	}
}
