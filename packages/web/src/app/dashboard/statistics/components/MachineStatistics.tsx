"use client";

import { trpc } from "@foodtools/core-web/src/trpc/client";
import { useState } from "react";

export function MachineStatistics() {
	const { data, isLoading } = trpc.statistics.machines.useQuery();
	const [expandedMachine, setExpandedMachine] = useState<string | null>(null);

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
					{data.statistics.map((stat, idx) => {
						const machineKey = `${stat.machineType}-${stat.machineModel}-${idx}`;
						const isExpanded = expandedMachine === machineKey;

						return (
							<MachineRow
								key={machineKey}
								stat={stat}
								machineKey={machineKey}
								isExpanded={isExpanded}
								onToggle={() =>
									setExpandedMachine(isExpanded ? null : machineKey)
								}
							/>
						);
					})}
				</tbody>
			</table>
		</div>
	);
}

function MachineRow({
	stat,
	machineKey,
	isExpanded,
	onToggle,
}: {
	stat: {
		machineType: string | null;
		machineModel: string | null;
		issueCount: number;
		totalHours: number;
	};
	machineKey: string;
	isExpanded: boolean;
	onToggle: () => void;
}) {
	const { data: partsData, isLoading: partsLoading } =
		trpc.statistics.machineParts.useQuery(
			{
				machineType: stat.machineType,
				machineModel: stat.machineModel,
			},
			{ enabled: isExpanded },
		);

	return (
		<>
			<tr
				className="border-b border-slate-800 hover:bg-slate-700/50 cursor-pointer"
				onClick={onToggle}
			>
				<td className="py-3 px-4 text-white">
					<div className="flex items-center gap-2">
						<svg
							className={`w-4 h-4 text-slate-400 transform transition-transform ${
								isExpanded ? "rotate-90" : ""
							}`}
							fill="none"
							viewBox="0 0 24 24"
							stroke="currentColor"
						>
							<path
								strokeLinecap="round"
								strokeLinejoin="round"
								strokeWidth={2}
								d="M9 5l7 7-7 7"
							/>
						</svg>
						{stat.machineType || "Unknown"}
					</div>
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
			{isExpanded && (
				<tr>
					<td colSpan={5} className="bg-slate-950/50 px-4 py-3">
						<div className="ml-6">
							<h4 className="text-sm font-medium text-slate-400 mb-3">
								Parts Used
							</h4>
							{partsLoading ? (
								<div className="text-slate-500 text-sm">Loading parts...</div>
							) : !partsData || partsData.length === 0 ? (
								<div className="text-slate-500 text-sm">No parts recorded</div>
							) : (
								<div className="space-y-2">
									{partsData.map((part) => (
										<div
											key={part.partName}
											className="flex justify-between items-center py-2 px-3 rounded bg-slate-800"
										>
											<span className="text-slate-300 capitalize">
												{part.partName}
											</span>
											<span className="text-white font-medium">
												{part.usageCount}{" "}
												{part.usageCount === 1 ? "time" : "times"}
											</span>
										</div>
									))}
								</div>
							)}
						</div>
					</td>
				</tr>
			)}
		</>
	);
}
