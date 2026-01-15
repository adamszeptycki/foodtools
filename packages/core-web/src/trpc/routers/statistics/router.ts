import {
	protectedProcedureWithOrganization,
	router,
} from "@foodtools/core-web/src/trpc/trpc";
import {
	getDashboardStats,
	getMachineParts,
	getMachineStats,
	getPartStats,
} from "./functions";
import { getMachinePartsSchema, getPartStatsSchema } from "./schema";

export const statisticsRouter = router({
	/**
	 * Get machine statistics with issue counts and labour hours
	 */
	machines: protectedProcedureWithOrganization.query(async ({ ctx }) => {
		return getMachineStats(ctx);
	}),

	/**
	 * Get part statistics with usage counts, machine breakdown, and hours
	 */
	parts: protectedProcedureWithOrganization
		.input(getPartStatsSchema.optional())
		.query(async ({ ctx, input }) => {
			return getPartStats(ctx, input || {});
		}),

	/**
	 * Get combined dashboard summary statistics
	 */
	dashboard: protectedProcedureWithOrganization.query(async ({ ctx }) => {
		return getDashboardStats(ctx);
	}),

	/**
	 * Get parts used by a specific machine
	 */
	machineParts: protectedProcedureWithOrganization
		.input(getMachinePartsSchema)
		.query(async ({ ctx, input }) => {
			return getMachineParts(ctx, input);
		}),
});
