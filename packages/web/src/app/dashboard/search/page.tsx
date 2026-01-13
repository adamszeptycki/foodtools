import { SemanticSearch } from "./components/SemanticSearch";

export default function SearchPage() {
	return (
		<div className="space-y-6">
			<h1 className="text-3xl font-semibold text-white">
				Search Service Reports
			</h1>
			<p className="text-lg text-slate-300">
				Describe a problem and find similar repairs from your service history
			</p>

			<SemanticSearch />
		</div>
	);
}
