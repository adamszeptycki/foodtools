"use client";

import { use } from "react";
import Link from "next/link";
import { trpc } from "@foodtools/core-web/src/trpc/client";

export default function DocumentDetailPage({
	params,
}: {
	params: Promise<{ id: string }>;
}) {
	const { id } = use(params);
	const { data: document, isLoading, error } = trpc.serviceDocuments.get.useQuery({ id });

	if (isLoading) {
		return (
			<div className="space-y-6">
				<BackLink />
				<div className="text-slate-400">Loading document...</div>
			</div>
		);
	}

	if (error || !document) {
		return (
			<div className="space-y-6">
				<BackLink />
				<div className="rounded-lg border border-red-800 bg-red-900/20 p-6">
					<p className="text-red-400">
						{error?.message || "Document not found"}
					</p>
				</div>
			</div>
		);
	}

	return (
		<div className="space-y-6">
			<BackLink />

			{/* Document Info */}
			<div className="rounded-lg border border-slate-700 bg-slate-800 p-6">
				<div className="flex items-start justify-between">
					<div>
						<h1 className="text-2xl font-semibold text-white">
							{document.fileName}
						</h1>
						<p className="text-sm text-slate-400 mt-1">
							Uploaded {new Date(document.createdAt).toLocaleString()}
						</p>
					</div>
					<StatusBadge status={document.processingStatus} />
				</div>

				<div className="mt-4 grid grid-cols-2 gap-4 text-sm">
					<div>
						<span className="text-slate-400">File Size:</span>
						<span className="text-white ml-2">
							{(document.fileSize / 1024 / 1024).toFixed(2)} MB
						</span>
					</div>
					<div>
						<span className="text-slate-400">Type:</span>
						<span className="text-white ml-2">{document.mimeType}</span>
					</div>
					{document.processedAt && (
						<div>
							<span className="text-slate-400">Processed:</span>
							<span className="text-white ml-2">
								{new Date(document.processedAt).toLocaleString()}
							</span>
						</div>
					)}
					{document.textLength && (
						<div>
							<span className="text-slate-400">Extracted Text:</span>
							<span className="text-white ml-2">
								{document.textLength.toLocaleString()} characters
							</span>
						</div>
					)}
				</div>

				{document.processingError && (
					<div className="mt-4 p-3 rounded-md bg-red-900/20 border border-red-800">
						<p className="text-sm text-red-400">
							<span className="font-medium">Error:</span> {document.processingError}
						</p>
					</div>
				)}
			</div>

			{/* Fixes */}
			{document.fixes && document.fixes.length > 0 && (
				<div className="rounded-lg border border-slate-700 bg-slate-800 p-6">
					<h2 className="text-xl font-semibold text-white mb-4">
						Extracted Fixes ({document.fixes.length})
					</h2>
					<div className="space-y-4">
						{document.fixes.map((fix) => (
							<div
								key={fix.id}
								className="p-4 rounded-lg border border-slate-600 bg-slate-700/50"
							>
								<div className="grid grid-cols-2 gap-4 text-sm">
									{fix.clientName && (
										<div>
											<span className="text-slate-400">Client:</span>
											<span className="text-white ml-2">{fix.clientName}</span>
										</div>
									)}
									{fix.machineModel && (
										<div>
											<span className="text-slate-400">Machine:</span>
											<span className="text-white ml-2">
												{fix.machineType} - {fix.machineModel}
											</span>
										</div>
									)}
									{fix.serviceDate && (
										<div>
											<span className="text-slate-400">Service Date:</span>
											<span className="text-white ml-2">
												{new Date(fix.serviceDate).toLocaleDateString()}
											</span>
										</div>
									)}
									{fix.labourHours && (
										<div>
											<span className="text-slate-400">Labour:</span>
											<span className="text-white ml-2">
												{fix.labourHours} hours
											</span>
										</div>
									)}
								</div>

								<div className="mt-3">
									<p className="text-slate-400 text-sm mb-1">Problem:</p>
									<p className="text-white">{fix.problemDescription}</p>
								</div>

								<div className="mt-3">
									<p className="text-slate-400 text-sm mb-1">Solution:</p>
									<p className="text-white">{fix.solutionApplied}</p>
								</div>

								{fix.partsUsed && (
									<div className="mt-3">
										<p className="text-slate-400 text-sm mb-1">Parts Used:</p>
										<p className="text-white">{fix.partsUsed}</p>
									</div>
								)}
							</div>
						))}
					</div>
				</div>
			)}

			{document.processingStatus === "completed" &&
				(!document.fixes || document.fixes.length === 0) && (
					<div className="rounded-lg border border-slate-700 bg-slate-800 p-6">
						<p className="text-slate-400 text-center">
							No fixes were extracted from this document.
						</p>
					</div>
				)}
		</div>
	);
}

function BackLink() {
	return (
		<Link
			href="/dashboard/documents"
			className="inline-flex items-center text-sm text-slate-400 hover:text-white transition-colors"
		>
			<svg
				className="w-4 h-4 mr-1"
				fill="none"
				viewBox="0 0 24 24"
				stroke="currentColor"
			>
				<path
					strokeLinecap="round"
					strokeLinejoin="round"
					strokeWidth={2}
					d="M15 19l-7-7 7-7"
				/>
			</svg>
			Back to Documents
		</Link>
	);
}

function StatusBadge({ status }: { status: string }) {
	const styles = {
		pending: "bg-yellow-900/30 text-yellow-400 border-yellow-800",
		processing: "bg-blue-900/30 text-blue-400 border-blue-800",
		completed: "bg-green-900/30 text-green-400 border-green-800",
		failed: "bg-red-900/30 text-red-400 border-red-800",
	};

	return (
		<span
			className={`px-3 py-1 text-xs font-medium rounded-full border ${
				styles[status as keyof typeof styles] || styles.pending
			}`}
		>
			{status}
		</span>
	);
}
