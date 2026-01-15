"use client";

import { trpc } from "@foodtools/core-web/src/trpc/client";

export function StatsSummary() {
	const { data, isLoading } = trpc.statistics.dashboard.useQuery();

	if (isLoading) {
		return (
			<div className="grid grid-cols-1 md:grid-cols-4 gap-4">
				{[1, 2, 3, 4].map((i) => (
					<div
						key={i}
						className="rounded-lg border border-slate-700 bg-slate-800 p-6 animate-pulse"
					>
						<div className="h-4 bg-slate-700 rounded w-24 mb-2" />
						<div className="h-8 bg-slate-700 rounded w-16" />
					</div>
				))}
			</div>
		);
	}

	const cards = [
		{ label: "Total Issues", value: data?.machines?.totalIssues ?? 0 },
		{
			label: "Total Hours",
			value: `${(data?.machines?.totalHours ?? 0).toFixed(1)}h`,
		},
		{ label: "Machine Types", value: data?.machines?.uniqueMachineTypes ?? 0 },
		{ label: "Unique Parts", value: data?.parts?.uniqueParts ?? 0 },
	];

	return (
		<div className="grid grid-cols-1 md:grid-cols-4 gap-4">
			{cards.map((card) => (
				<div
					key={card.label}
					className="rounded-lg border border-slate-700 bg-slate-800 p-6"
				>
					<p className="text-sm text-slate-400">{card.label}</p>
					<p className="text-2xl font-bold text-white mt-1">{card.value}</p>
				</div>
			))}
		</div>
	);
}
