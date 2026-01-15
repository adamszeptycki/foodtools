import type { Context } from "@foodtools/core-web/src/trpc/context";
import {
	getMachineStatistics,
	getMachineSummary,
	getPartStatistics,
	getPartsSummary,
} from "@foodtools/core/src/sql/queries/service-documents/statistics";

type ProtectedContextWithOrganization = Context & {
	session: NonNullable<Context["session"]>;
	organization: {
		members: Array<{
			userId: string;
			user?: { id?: string; name?: string; email?: string; image?: string };
		}>;
	};
};

/**
 * Get user IDs for all members in the organization
 */
function getOrganizationMemberIds(ctx: ProtectedContextWithOrganization): string[] {
	const members = ctx.organization?.members ?? [];

	if (members.length === 0) {
		// Fallback: if no members found, use current user's ID
		return [ctx.session.user.id];
	}

	return members
		.map((m: any) => m.userId ?? m.user?.id)
		.filter((id): id is string => Boolean(id));
}

/**
 * Get machine statistics for the organization
 */
export async function getMachineStats(ctx: ProtectedContextWithOrganization) {
	const memberIds = getOrganizationMemberIds(ctx);

	const [statistics, summary] = await Promise.all([
		getMachineStatistics(memberIds),
		getMachineSummary(memberIds),
	]);

	return { statistics, summary };
}

/**
 * Get part statistics for the organization
 */
export async function getPartStats(
	ctx: ProtectedContextWithOrganization,
	input: { limit?: number } = {},
) {
	const memberIds = getOrganizationMemberIds(ctx);

	const [statistics, summary] = await Promise.all([
		getPartStatistics(memberIds),
		getPartsSummary(memberIds),
	]);

	const limitedStats = input.limit
		? statistics.slice(0, input.limit)
		: statistics;

	return { statistics: limitedStats, summary };
}

/**
 * Get combined dashboard statistics
 */
export async function getDashboardStats(ctx: ProtectedContextWithOrganization) {
	const memberIds = getOrganizationMemberIds(ctx);

	const [machineSummary, partsSummary] = await Promise.all([
		getMachineSummary(memberIds),
		getPartsSummary(memberIds),
	]);

	return {
		machines: machineSummary,
		parts: partsSummary,
	};
}
