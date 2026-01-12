import OpenAI from "openai";
import { Resource } from "sst";
import { z } from "zod";

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

// Schema for a single fix
const FixSchema = z.object({
	machineModel: z.string().nullable(),
	machineType: z.string().nullable(),
	problemDescription: z.string(),
	solutionApplied: z.string(),
	partsUsed: z.string().nullable(),
	clientName: z.string().nullable(),
	serviceDate: z.string().nullable(), // ISO date string
});

// Schema for the response containing fixes array
const FixesResponseSchema = z.object({
	fixes: z.array(FixSchema),
});

export type ExtractedFix = z.infer<typeof FixSchema>;

/**
 * Extract structured data from service document text using OpenAI GPT-4o-mini
 * @param text - Raw text extracted from PDF
 * @returns Array of extracted fix records
 */
export async function extractStructuredData(
	text: string,
): Promise<ExtractedFix[]> {
	const prompt = `You are an expert at extracting structured information from machine service documents.

Analyze the following service document and extract ALL machine repair/fix records mentioned.
For each fix, extract:
- machineModel: The specific model number or name of the machine
- machineType: The type/category of machine (e.g., "CNC Mill", "Pump", "Compressor", "Motor")
- problemDescription: What was wrong with the machine
- solutionApplied: How the problem was fixed
- partsUsed: List of parts that were replaced or used (can be comma-separated)
- clientName: Name of the client/customer
- serviceDate: Date of service (if mentioned, in ISO format YYYY-MM-DD)

If multiple fixes are described in the document, extract them as separate objects in the fixes array.
If information is not available, use null for that field.

Document text:
${text}

Return the result as a JSON object with a "fixes" array containing all extracted fix objects.`;

	try {
		const response = await openai.chat.completions.create({
			model: "gpt-4o-mini",
			messages: [
				{
					role: "system",
					content:
						"You extract structured data from service documents. Always respond with valid JSON.",
				},
				{
					role: "user",
					content: prompt,
				},
			],
			response_format: { type: "json_object" },
			temperature: 0.1, // Low temperature for consistency
		});

		const content = response.choices[0].message.content;
		if (!content) {
			throw new Error("No content in OpenAI response");
		}

		const parsed = JSON.parse(content);

		// Validate with Zod
		const validated = FixesResponseSchema.parse(parsed);

		return validated.fixes;
	} catch (error) {
		console.error("Error extracting structured data:", error);
		throw new Error(
			`Failed to extract structured data: ${error instanceof Error ? error.message : "Unknown error"}`,
		);
	}
}
