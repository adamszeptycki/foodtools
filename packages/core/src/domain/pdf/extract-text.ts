import { extractText } from "unpdf";

/**
 * Extract text content from a PDF buffer using unpdf
 * @param buffer - PDF file as a Buffer
 * @returns Extracted text content
 */
export async function extractTextFromPDF(buffer: Buffer): Promise<string> {
	try {
		// Convert Buffer to Uint8Array as required by unpdf
		const uint8Array = new Uint8Array(buffer);
		const { text } = await extractText(uint8Array);
		// text is an array of strings (one per page), join them
		return Array.isArray(text) ? text.join("\n") : text;
	} catch (error) {
		console.error("Error extracting text from PDF:", error);
		throw new Error(
			`Failed to extract text from PDF: ${error instanceof Error ? error.message : "Unknown error"}`,
		);
	}
}
