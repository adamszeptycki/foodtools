"use client";

import { useState } from "react";
import { trpc } from "@foodtools/core-web/src/trpc/client";

export function SemanticSearch() {
	const [query, setQuery] = useState("");
	const [hasSearched, setHasSearched] = useState(false);

	const searchMutation = trpc.serviceDocuments.semanticSearch.useMutation();

	const handleSearch = async (e: React.FormEvent) => {
		e.preventDefault();
		if (!query.trim()) return;

		setHasSearched(true);
		await searchMutation.mutateAsync({
			query,
			limit: 10,
			minSimilarity: 0.7,
		});
	};

	const results = searchMutation.data || [];

	return (
		<div className="space-y-6">
			<div className="rounded-lg border border-slate-700 bg-slate-800 p-6">
				<h2 className="text-xl font-semibold text-white mb-4">
					Search Similar Fixes
				</h2>

				<form onSubmit={handleSearch} className="space-y-4">
					<div>
						<label className="block text-sm font-medium text-slate-300 mb-2">
							Describe the problem you're facing
						</label>
						<textarea
							value={query}
							onChange={(e) => setQuery(e.target.value)}
							placeholder="e.g., Motor making grinding noise and overheating"
							rows={3}
							className="w-full rounded-md border border-slate-600 bg-slate-900
                px-4 py-2 text-white placeholder-slate-500
                focus:border-blue-500 focus:outline-none"
						/>
					</div>

					<button
						type="submit"
						disabled={searchMutation.isPending || !query.trim()}
						className="px-6 py-2 bg-blue-600 text-white rounded-md
              hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed
              transition-colors"
					>
						{searchMutation.isPending ? "Searching..." : "Search"}
					</button>
				</form>
			</div>

			{searchMutation.isError && (
				<div className="text-sm text-red-400 bg-red-900/20 border border-red-800 rounded p-4">
					Error: {searchMutation.error.message}
				</div>
			)}

			{hasSearched && results.length > 0 && (
				<div className="space-y-4">
					<h3 className="text-lg font-semibold text-white">
						Similar Fixes ({results.length})
					</h3>

					{results.map((result) => (
						<div
							key={result.id}
							className="rounded-lg border border-slate-700 bg-slate-800 p-5"
						>
							<div className="flex items-start justify-between mb-3">
								<div>
									<h4 className="text-white font-medium">
										{result.machineModel || "Unknown Model"}
										{result.machineType && (
											<span className="text-slate-400 text-sm ml-2">
												({result.machineType})
											</span>
										)}
									</h4>
									{result.clientName && (
										<p className="text-sm text-slate-400">
											Client: {result.clientName}
										</p>
									)}
								</div>

								<div className="text-right">
									<div className="text-sm text-blue-400 font-medium">
										{((result.similarity ?? 0) * 100).toFixed(1)}% match
									</div>
								</div>
							</div>

							<div className="space-y-3 text-sm">
								<div>
									<span className="text-slate-400 font-medium">Problem:</span>
									<p className="text-slate-200 mt-1">
										{result.problemDescription}
									</p>
								</div>

								<div>
									<span className="text-slate-400 font-medium">Solution:</span>
									<p className="text-slate-200 mt-1">
										{result.solutionApplied}
									</p>
								</div>

								{result.partsUsed && (
									<div>
										<span className="text-slate-400 font-medium">
											Parts Used:
										</span>
										<p className="text-slate-200 mt-1">{result.partsUsed}</p>
									</div>
								)}
							</div>
						</div>
					))}
				</div>
			)}

			{hasSearched && searchMutation.isSuccess && results.length === 0 && (
				<div className="text-center text-slate-400 py-8">
					No similar fixes found. Try adjusting your search.
				</div>
			)}
		</div>
	);
}
