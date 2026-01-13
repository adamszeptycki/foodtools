import { z } from "zod";

export const CreateTenantSchema = z.object({
	name: z.string().min(1),
	domain: z.string().min(1),
	type: z.enum(["company", "individual"]).default("company"),
	logo: z.string().optional(),
});
export type CreateTenantArgs = z.infer<typeof CreateTenantSchema>;

export const initiateLogoUploadSchema = z.object({
	fileName: z.string().min(1).max(255),
	fileSize: z.number().positive().max(5 * 1024 * 1024), // Max 5MB
	mimeType: z.string().regex(/^image\/(png|jpeg|webp)$/),
});
