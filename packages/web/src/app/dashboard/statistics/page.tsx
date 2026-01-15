import { StatsSummary } from "./components/StatsSummary";
import { MachineStatistics } from "./components/MachineStatistics";
import { PartStatistics } from "./components/PartStatistics";

export default function StatisticsPage() {
	return (
		<div className="space-y-6">
			<h1 className="text-2xl font-semibold text-white">Service Statistics</h1>

			<StatsSummary />

			<div className="rounded-lg border border-slate-700 bg-slate-800 p-6">
				<h2 className="text-xl font-semibold text-white mb-4">
					Machine Statistics
				</h2>
				<MachineStatistics />
			</div>

			<div className="rounded-lg border border-slate-700 bg-slate-800 p-6">
				<h2 className="text-xl font-semibold text-white mb-4">
					Part Statistics
				</h2>
				<PartStatistics />
			</div>
		</div>
	);
}
