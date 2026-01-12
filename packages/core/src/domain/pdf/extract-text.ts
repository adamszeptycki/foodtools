import pdf from "pdf-parse";

/**
 * Extract text content from a PDF buffer using pdf-parse
 * @param buffer - PDF file as a Buffer
 * @returns Extracted text content
 */
export async function extractTextFromPDF(buffer: Buffer): Promise<string> {
	try {
		const data = await pdf(buffer);
		return data.text;
	} catch (error) {
		console.error("Error extracting text from PDF:", error);
		throw new Error(
			`Failed to extract text from PDF: ${error instanceof Error ? error.message : "Unknown error"}`,
		);
	}
}
