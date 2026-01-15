import { z } from "zod";

export const getPartStatsSchema = z.object({
	limit: z.number().min(1).max(100).default(50),
});
