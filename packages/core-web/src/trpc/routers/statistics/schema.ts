import { z } from "zod";

export const getPartStatsSchema = z.object({
	limit: z.number().min(1).max(100).default(50),
});

export const getMachinePartsSchema = z.object({
	machineType: z.string().nullable(),
	machineModel: z.string().nullable(),
});
