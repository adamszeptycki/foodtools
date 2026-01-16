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
 * Summarize a problem description for better embedding search
 * Focuses on capturing main problems, using standard technical terminology,
 * and removing unnecessary context/dates/client details
 *
 * @param problemDescription - The original problem description text
 * @returns A concise 50-100 word summary focused on symptoms and failure modes
 */
export async function summarizeProblemDescription(
	problemDescription: string,
): Promise<string> {
	const prompt = `You are a technical documentation specialist. Summarize the following machine service problem description for optimal semantic search matching.

GUIDELINES:
- Capture the main problem(s) only
- Use standard technical terminology
- Remove unnecessary context, dates, client details, and names
- Focus on symptoms, failure modes, and affected components
- Keep the summary between 50-100 words
- Use clear, searchable language that would match similar problems

ORIGINAL PROBLEM DESCRIPTION:
${problemDescription}

SUMMARY:`;

	try {
		const response = await openai.chat.completions.create({
			model: "gpt-4o-mini",
			messages: [
				{
					role: "system",
					content:
						"You create concise, searchable technical summaries of machine problems. Focus on symptoms and failure modes using standard terminology.",
				},
				{
					role: "user",
					content: prompt,
				},
			],
			temperature: 0.3, // Low temperature for consistency
			max_tokens: 200,
		});

		const summary = response.choices[0]?.message?.content?.trim();
		if (!summary) {
			console.warn("Empty summary returned, using original text");
			return problemDescription;
		}

		return summary;
	} catch (error) {
		console.error("Error summarizing problem description:", error);
		// Fallback to original text if summarization fails
		return problemDescription;
	}
}
