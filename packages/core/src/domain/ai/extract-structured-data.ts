import OpenAI from "openai";
import { zodResponseFormat } from "openai/helpers/zod";
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

// Schema for a single fix with all extracted data
const FixSchema = z.object({
	// Client Info
	clientName: z.string().nullable(),
	clientAddress: z.string().nullable(),
	clientPhone: z.string().nullable(),

	// Equipment Info
	machineModel: z.string().nullable(),
	machineType: z.string().nullable(),
	serialNumber: z.string().nullable(),

	// Service Details
	problemDescription: z.string(),
	solutionApplied: z.string(),
	partsUsed: z.string().nullable(),
	serviceDate: z.string().nullable(), // ISO date string

	// Technician Info
	technicianName: z.string().nullable(),
	technicianId: z.string().nullable(),

	// Labour
	labourHours: z.number().nullable(),
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

Analyze the following service document and extract the machine repair/fix record.
Extract the following information:

CLIENT INFORMATION:
- clientName: Name of the client/customer
- clientAddress: Full address of the client (street, city, state, zip)
- clientPhone: Phone number of the client

EQUIPMENT INFORMATION:
- machineModel: The specific model number or name of the machine
- machineType: The type/category of machine (e.g., "CNC Mill", "Pump", "Compressor", "Motor")
- serialNumber: The serial number of the equipment

SERVICE DETAILS:
- problemDescription: What was wrong with the machine (detailed description)
- solutionApplied: How the problem was fixed (detailed description)
- partsUsed: List of parts that were replaced or used (can be comma-separated)
- serviceDate: Date of service (in ISO format YYYY-MM-DD)

TECHNICIAN INFORMATION:
- technicianName: Name of the technician who performed the service
- technicianId: Employee ID or badge number of the technician

LABOUR:
- labourHours: Total hours worked on the repair (as a number)

If information is not available, use null for that field.
For labourHours, extract the numeric value only (e.g., 2.5 not "2.5 hours").

Document text:
${text}

Return the result as a JSON object with a "fixes" array containing the extracted fix object.`;

	try {
		const response = await openai.chat.completions.parse({
			model: "gpt-4o-mini",
			messages: [
				{
					role: "system",
					content: "You extract structured data from service documents.",
				},
				{
					role: "user",
					content: prompt,
				},
			],
			response_format: zodResponseFormat(FixesResponseSchema, "fixes_response"),
			temperature: 0.1, // Low temperature for consistency
		});

		const parsed = response.choices[0].message.parsed;
		if (!parsed) {
			throw new Error("No parsed content in OpenAI response");
		}

		return parsed.fixes;
	} catch (error) {
		console.error("Error extracting structured data:", error);
		throw new Error(
			`Failed to extract structured data: ${error instanceof Error ? error.message : "Unknown error"}`,
		);
	}
}
