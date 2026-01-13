"use client";

import { trpc } from "@foodtools/core-web/src/trpc/client";
import { useState } from "react";

export function SemanticSearch() {
	const [query, setQuery] = useState("");
	const [hasSearched, setHasSearched] = useState(false);
	const [loadingDocId, setLoadingDocId] = useState<string | null>(null);

	const searchMutation = trpc.serviceDocuments.semanticSearch.useMutation();
	const utils = trpc.useUtils();

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

	const handleViewDocument = async (documentId: string) => {
		setLoadingDocId(documentId);
		try {
			const { url } = await utils.serviceDocuments.getDocumentUrl.fetch({
				documentId,
			});
			window.open(url, "_blank");
		} catch (error) {
			console.error("Failed to get document URL:", error);
		} finally {
			setLoadingDocId(null);
		}
	};

	const results = searchMutation.data || [];

	// Parse comma-separated parts into array of items
	const parsePartsUsed = (partsUsed: string | null) => {
		if (!partsUsed) return [];
		return partsUsed
			.split(",")
			.map((part) => part.trim())
			.filter((part) => part.length > 0);
	};

	return (
		<div className="space-y-8">
			<div className="rounded-lg border border-slate-700 bg-slate-800 p-6">
				<h2 className="text-2xl font-semibold text-white mb-4">
					Search Similar Fixes
				</h2>

				<form onSubmit={handleSearch} className="space-y-4">
					<div>
						<label htmlFor="query" className="block text-base font-medium text-slate-300 mb-2">
							Describe the problem you&apos;re facing
						</label>
						<textarea
							value={query}
							onChange={(e) => setQuery(e.target.value)}
							placeholder="e.g., Motor making grinding noise and overheating"
							rows={3}
							className="w-full rounded-md border border-slate-600 bg-slate-900
                px-4 py-3 text-lg text-white placeholder-slate-500
                focus:border-blue-500 focus:outline-none"
						/>
					</div>

					<button
						type="submit"
						disabled={searchMutation.isPending || !query.trim()}
						className="px-6 py-3 text-lg bg-blue-600 text-white rounded-md
              hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed
              transition-colors"
					>
						{searchMutation.isPending ? "Searching..." : "Search"}
					</button>
				</form>
			</div>

			{searchMutation.isError && (
				<div className="text-base text-red-400 bg-red-900/20 border border-red-800 rounded p-4">
					Error: {searchMutation.error.message}
				</div>
			)}

			{hasSearched && results.length > 0 && (
				<div className="space-y-5">
					<h3 className="text-xl font-semibold text-white">
						Similar Fixes ({results.length})
					</h3>

					{results.map((result) => {
						const parts = parsePartsUsed(result.partsUsed);

						return (
							<div
								key={result.id}
								className="rounded-lg border border-slate-700 bg-slate-800 p-6"
							>
								<div className="flex items-start justify-between mb-4">
									<div>
										<h4 className="text-lg text-white font-medium">
											{result.machineModel || "Unknown Model"}
											{result.machineType && (
												<span className="text-slate-400 text-base ml-2">
													({result.machineType})
												</span>
											)}
										</h4>
										{result.clientName && (
											<p className="text-base text-slate-400">
												Client: {result.clientName}
											</p>
										)}
									</div>

									<div className="text-right flex flex-col items-end gap-2">
										<div className="text-base text-blue-400 font-medium">
											{((result.similarity ?? 0) * 100).toFixed(1)}% match
										</div>
										<button
											onClick={() => handleViewDocument(result.documentId)}
											disabled={loadingDocId === result.documentId}
											className="text-base text-slate-300 hover:text-white underline transition-colors disabled:opacity-50"
										>
											{loadingDocId === result.documentId ? "Loading..." : "View PDF"}
										</button>
									</div>
								</div>

								<div className="space-y-4">
									<div>
										<span className="text-base text-slate-400 font-medium">Problem:</span>
										<p className="text-base text-slate-200 mt-1">
											{result.problemDescription}
										</p>
									</div>

									<div>
										<span className="text-base text-slate-400 font-medium">Solution:</span>
										<p className="text-base text-slate-200 mt-1">
											{result.solutionApplied}
										</p>
									</div>

									{result.labourHours != null && (
										<div>
											<span className="text-base text-slate-400 font-medium">Labour Hours:</span>
											<p className="text-base text-slate-200 mt-1">
												{result.labourHours} {result.labourHours === 1 ? "hour" : "hours"}
											</p>
										</div>
									)}

									{parts.length > 0 && (
										<div>
											<span className="text-base text-slate-400 font-medium">Parts Used:</span>
											<ul className="mt-2 space-y-1">
												{parts.map((part, index) => (
													<li key={index} className="text-base text-slate-200 flex items-start">
														<span className="text-slate-500 mr-2">•</span>
														{part}
													</li>
												))}
											</ul>
										</div>
									)}
								</div>
							</div>
						);
					})}
				</div>
			)}

			{hasSearched && searchMutation.isSuccess && results.length === 0 && (
				<div className="text-center text-lg text-slate-400 py-8">
					No similar fixes found. Try adjusting your search.
				</div>
			)}
		</div>
	);
}
