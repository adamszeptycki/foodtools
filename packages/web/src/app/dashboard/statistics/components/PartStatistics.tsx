"use client";

import { trpc } from "@foodtools/core-web/src/trpc/client";
import { useState } from "react";

export function PartStatistics() {
	const { data, isLoading } = trpc.statistics.parts.useQuery({ limit: 50 });
	const [expandedPart, setExpandedPart] = useState<string | null>(null);

	if (isLoading) {
		return <div className="text-slate-400">Loading part statistics...</div>;
	}

	if (!data || data.statistics.length === 0) {
		return (
			<div className="text-slate-400 text-center py-8">
				No part data available yet
			</div>
		);
	}

	return (
		<div className="space-y-3">
			{data.statistics.map((part) => (
				<div
					key={part.partName}
					className="rounded-lg border border-slate-700 bg-slate-900"
				>
					<button
						type="button"
						onClick={() =>
							setExpandedPart(
								expandedPart === part.partName ? null : part.partName,
							)
						}
						className="w-full p-4 flex items-center justify-between hover:bg-slate-800/50 transition-colors"
					>
						<div className="flex items-center gap-4">
							<span className="text-white font-medium capitalize">
								{part.partName}
							</span>
							
						</div>
						<div className="flex items-center gap-6">
						<span className="text-sm text-slate-400">
								{part.machineBreakdown.length} machine(s)
							</span>
							<div className="text-right">
								<span className="text-white font-medium">{part.usageCount}</span>
								<span className="text-slate-400 text-sm ml-1">uses</span>
							</div>
							<div className="text-right">
								<span className="text-slate-300">
									{part.totalHours.toFixed(1)}
								</span>
								<span className="text-slate-400 text-sm ml-1">hours</span>
							</div>
							<svg
								className={`w-5 h-5 text-slate-400 transform transition-transform ${
									expandedPart === part.partName ? "rotate-180" : ""
								}`}
								fill="none"
								viewBox="0 0 24 24"
								stroke="currentColor"
							>
								<path
									strokeLinecap="round"
									strokeLinejoin="round"
									strokeWidth={2}
									d="M19 9l-7 7-7-7"
								/>
							</svg>
						</div>
					</button>

					{expandedPart === part.partName && (
						<div className="border-t border-slate-700 p-4 bg-slate-950/50">
							<h4 className="text-sm font-medium text-slate-400 mb-3">
								Machine Breakdown
							</h4>
							<div className="space-y-2">
								{part.machineBreakdown.map((machine, idx) => (
									<div
										key={`${machine.machineType}-${machine.machineModel}-${idx}`}
										className="flex justify-between items-center py-2 px-3 rounded bg-slate-800"
									>
										<span className="text-slate-300">
											{machine.machineType} - {machine.machineModel}
										</span>
										<span className="text-white font-medium">
											{machine.count} {machine.count === 1 ? "time" : "times"}
										</span>
									</div>
								))}
							</div>
						</div>
					)}
				</div>
			))}
		</div>
	);
}
