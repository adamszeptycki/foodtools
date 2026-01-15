import { getDb } from "@foodtools/core/src/sql";
import { machineFixes } from "@foodtools/core/src/sql/schema";
import { and, inArray, isNotNull, sql } from "drizzle-orm";

/**
 * Get machine statistics aggregated by machine type and model
 * Returns: issue count and total labour hours per machine type/model
 */
export async function getMachineStatistics(userIds: string[]) {
	if (userIds.length === 0) {
		return [];
	}

	const db = getDb();

	const results = await db
		.select({
			machineType: machineFixes.machineType,
			machineModel: machineFixes.machineModel,
			issueCount: sql<number>`count(*)::int`.as("issue_count"),
			totalHours: sql<number>`COALESCE(SUM(${machineFixes.labourHours}), 0)`.as(
				"total_hours",
			),
		})
		.from(machineFixes)
		.where(inArray(machineFixes.userId, userIds))
		.groupBy(machineFixes.machineType, machineFixes.machineModel)
		.orderBy(sql`count(*) DESC`);

	return results;
}

/**
 * Get summary statistics for all machines
 */
export async function getMachineSummary(userIds: string[]) {
	if (userIds.length === 0) {
		return {
			totalIssues: 0,
			totalHours: 0,
			uniqueMachineTypes: 0,
			uniqueMachineModels: 0,
		};
	}

	const db = getDb();

	const [result] = await db
		.select({
			totalIssues: sql<number>`count(*)::int`.as("total_issues"),
			totalHours: sql<number>`COALESCE(SUM(${machineFixes.labourHours}), 0)`.as(
				"total_hours",
			),
			uniqueMachineTypes:
				sql<number>`COUNT(DISTINCT ${machineFixes.machineType})::int`.as(
					"unique_types",
				),
			uniqueMachineModels:
				sql<number>`COUNT(DISTINCT ${machineFixes.machineModel})::int`.as(
					"unique_models",
				),
		})
		.from(machineFixes)
		.where(inArray(machineFixes.userId, userIds));

	return (
		result ?? {
			totalIssues: 0,
			totalHours: 0,
			uniqueMachineTypes: 0,
			uniqueMachineModels: 0,
		}
	);
}

/**
 * Get all fixes with parts data for aggregation
 */
export async function getFixesWithParts(userIds: string[]) {
	if (userIds.length === 0) {
		return [];
	}

	const db = getDb();

	const fixes = await db
		.select({
			id: machineFixes.id,
			partsUsed: machineFixes.partsUsed,
			machineType: machineFixes.machineType,
			machineModel: machineFixes.machineModel,
			labourHours: machineFixes.labourHours,
		})
		.from(machineFixes)
		.where(
			and(
				inArray(machineFixes.userId, userIds),
				isNotNull(machineFixes.partsUsed),
				sql`${machineFixes.partsUsed} != ''`,
			),
		);

	return fixes;
}

/**
 * Aggregate part statistics from fixes data
 * Parses comma-separated parts_used field and aggregates by part name
 */
export function aggregatePartStatistics(
	fixes: Array<{
		id: string;
		partsUsed: string | null;
		machineType: string | null;
		machineModel: string | null;
		labourHours: number | null;
	}>,
) {
	const partsMap = new Map<
		string,
		{
			partName: string;
			usageCount: number;
			totalHours: number;
			machines: Map<
				string,
				{ machineType: string; machineModel: string; count: number }
			>;
		}
	>();

	for (const fix of fixes) {
		if (!fix.partsUsed) continue;

		const parts = fix.partsUsed
			.split(",")
			.map((p) => p.trim())
			.filter((p) => p.length > 0);

		for (const partName of parts) {
			const normalizedPart = partName.toLowerCase();
			const existing = partsMap.get(normalizedPart);
			const machineKey = `${fix.machineType || "Unknown"}|${fix.machineModel || "Unknown"}`;

			if (existing) {
				existing.usageCount++;
				existing.totalHours += fix.labourHours || 0;

				const machineEntry = existing.machines.get(machineKey);
				if (machineEntry) {
					machineEntry.count++;
				} else {
					existing.machines.set(machineKey, {
						machineType: fix.machineType || "Unknown",
						machineModel: fix.machineModel || "Unknown",
						count: 1,
					});
				}
			} else {
				const machines = new Map();
				machines.set(machineKey, {
					machineType: fix.machineType || "Unknown",
					machineModel: fix.machineModel || "Unknown",
					count: 1,
				});
				partsMap.set(normalizedPart, {
					partName: partName, // Keep original casing for display
					usageCount: 1,
					totalHours: fix.labourHours || 0,
					machines,
				});
			}
		}
	}

	// Convert to array format
	return Array.from(partsMap.values())
		.map((part) => ({
			partName: part.partName,
			usageCount: part.usageCount,
			totalHours: part.totalHours,
			machineBreakdown: Array.from(part.machines.values()),
		}))
		.sort((a, b) => b.usageCount - a.usageCount);
}

/**
 * Get part statistics - parsed from comma-separated parts_used field
 */
export async function getPartStatistics(userIds: string[]) {
	const fixes = await getFixesWithParts(userIds);
	return aggregatePartStatistics(fixes);
}

/**
 * Get parts summary statistics
 */
export async function getPartsSummary(userIds: string[]) {
	const partStats = await getPartStatistics(userIds);

	return {
		uniqueParts: partStats.length,
		totalPartUsages: partStats.reduce((sum, p) => sum + p.usageCount, 0),
		totalHoursOnParts: partStats.reduce((sum, p) => sum + p.totalHours, 0),
	};
}
