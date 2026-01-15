"use client";

import { useState } from "react";
import { MachineStatistics } from "./components/MachineStatistics";
import { PartStatistics } from "./components/PartStatistics";
import { StatsSummary } from "./components/StatsSummary";

export default function StatisticsPage() {
	const [activeTab, setActiveTab] = useState<"machines" | "parts">("machines");

	return (
		<div className="space-y-6">
			<h1 className="text-2xl font-semibold text-white">Service Statistics</h1>

			<StatsSummary />

			<div className="rounded-lg border border-slate-700 bg-slate-800">
				{/* Tab buttons */}
				<div className="flex border-b border-slate-700">
					<button
						onClick={() => setActiveTab("machines")}
						className={`px-6 py-3 text-sm font-medium transition-colors ${
							activeTab === "machines"
								? "text-white border-b-2 border-blue-500 -mb-px"
								: "text-slate-400 hover:text-slate-200"
						}`}
					>
						Machines
					</button>
					<button
						onClick={() => setActiveTab("parts")}
						className={`px-6 py-3 text-sm font-medium transition-colors ${
							activeTab === "parts"
								? "text-white border-b-2 border-blue-500 -mb-px"
								: "text-slate-400 hover:text-slate-200"
						}`}
					>
						Parts
					</button>
				</div>

				{/* Tab content */}
				<div className="p-6">
					{activeTab === "machines" ? (
						<MachineStatistics />
					) : (
						<PartStatistics />
					)}
				</div>
			</div>
		</div>
	);
}
