import { SemanticSearch } from "./components/SemanticSearch";

export default function SearchPage() {
	return (
		<div className="space-y-4">
			<h1 className="text-2xl font-semibold text-white">
				Find Similar Fixes
			</h1>
			<p className="text-slate-300">
				Describe a problem and find similar repairs from your service history
			</p>

			<SemanticSearch />
		</div>
	);
}
