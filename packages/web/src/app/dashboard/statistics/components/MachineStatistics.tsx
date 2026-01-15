"use client";

import { trpc } from "@foodtools/core-web/src/trpc/client";

export function MachineStatistics() {
	const { data, isLoading } = trpc.statistics.machines.useQuery();

	if (isLoading) {
		return <div className="text-slate-400">Loading machine statistics...</div>;
	}

	if (!data || data.statistics.length === 0) {
		return (
			<div className="text-slate-400 text-center py-8">
				No machine data available yet
			</div>
		);
	}

	return (
		<div className="overflow-x-auto">
			<table className="w-full">
				<thead>
					<tr className="border-b border-slate-700">
						<th className="text-left text-slate-300 font-medium py-3 px-4">
							Machine Type
						</th>
						<th className="text-left text-slate-300 font-medium py-3 px-4">
							Model
						</th>
						<th className="text-right text-slate-300 font-medium py-3 px-4">
							Issues
						</th>
						<th className="text-right text-slate-300 font-medium py-3 px-4">
							Total Hours
						</th>
						<th className="text-right text-slate-300 font-medium py-3 px-4">
							Avg Hours/Issue
						</th>
					</tr>
				</thead>
				<tbody>
					{data.statistics.map((stat, idx) => (
						<tr
							key={`${stat.machineType}-${stat.machineModel}-${idx}`}
							className="border-b border-slate-800 hover:bg-slate-700/50"
						>
							<td className="py-3 px-4 text-white">
								{stat.machineType || "Unknown"}
							</td>
							<td className="py-3 px-4 text-slate-300">
								{stat.machineModel || "Unknown"}
							</td>
							<td className="py-3 px-4 text-right text-white font-medium">
								{stat.issueCount}
							</td>
							<td className="py-3 px-4 text-right text-slate-300">
								{stat.totalHours.toFixed(1)}h
							</td>
							<td className="py-3 px-4 text-right text-slate-400">
								{stat.issueCount > 0
									? (stat.totalHours / stat.issueCount).toFixed(1)
									: "0"}
								h
							</td>
						</tr>
					))}
				</tbody>
			</table>
		</div>
	);
}
