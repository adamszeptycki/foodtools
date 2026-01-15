"use client";

import { useState } from "react";
import { trpc } from "@foodtools/core-web/src/trpc/client";
import Link from "next/link";

const PAGE_SIZE = 10;

type StatusFilter = "all" | "pending" | "processing" | "completed" | "failed";

const TAB_CONFIG: { key: StatusFilter; label: string }[] = [
	{ key: "all", label: "All" },
	{ key: "pending", label: "Pending" },
	{ key: "processing", label: "Processing" },
	{ key: "completed", label: "Completed" },
	{ key: "failed", label: "Failed" },
];

export function DocumentList() {
	const [page, setPage] = useState(0);
	const [activeStatus, setActiveStatus] = useState<StatusFilter>("all");
	const utils = trpc.useUtils();

	const { data: statusCounts } = trpc.serviceDocuments.statusCounts.useQuery();

	const { data, isLoading } = trpc.serviceDocuments.list.useQuery({
		limit: PAGE_SIZE,
		offset: page * PAGE_SIZE,
		status: activeStatus === "all" ? undefined : activeStatus,
	});

	const reprocessMutation = trpc.serviceDocuments.reprocess.useMutation({
		onSuccess: () => {
			utils.serviceDocuments.list.invalidate();
			utils.serviceDocuments.statusCounts.invalidate();
		},
	});

	const handleStatusChange = (status: StatusFilter) => {
		setActiveStatus(status);
		setPage(0);
	};

	const handleReprocess = (
		e: React.MouseEvent,
		documentId: string,
	) => {
		e.preventDefault();
		e.stopPropagation();
		reprocessMutation.mutate({ documentId });
	};

	const renderTabs = () => (
		<div className="flex border-b border-slate-700 mb-4">
			{TAB_CONFIG.map(({ key, label }) => (
				<button
					key={key}
					onClick={() => handleStatusChange(key)}
					className={`px-4 py-2 text-sm font-medium transition-colors flex items-center gap-2 ${
						activeStatus === key
							? "text-white border-b-2 border-blue-500 -mb-px"
							: "text-slate-400 hover:text-slate-200"
					}`}
				>
					{label}
					{statusCounts && (
						<span
							className={`px-2 py-0.5 text-xs rounded-full ${
								activeStatus === key
									? "bg-blue-600 text-white"
									: "bg-slate-700 text-slate-300"
							}`}
						>
							{statusCounts[key]}
						</span>
					)}
				</button>
			))}
		</div>
	);

	if (isLoading) {
		return (
			<div>
				{renderTabs()}
				<div className="text-slate-400">Loading documents...</div>
			</div>
		);
	}

	if (!data || data.documents.length === 0) {
		const emptyMessage =
			activeStatus === "all"
				? "No documents uploaded yet"
				: `No ${activeStatus} documents`;

		return (
			<div>
				{renderTabs()}
				<div className="text-slate-400 text-center py-8">{emptyMessage}</div>
			</div>
		);
	}

	const { documents, total } = data;
	const totalPages = Math.ceil(total / PAGE_SIZE);
	const hasPrev = page > 0;
	const hasNext = page < totalPages - 1;

	return (
		<div className="space-y-4">
			{renderTabs()}
			<div className="space-y-3">
				{documents.map((doc) => (
					<Link
						key={doc.id}
						href={`/dashboard/documents/${doc.id}`}
						className="block rounded-lg border border-slate-700 bg-slate-800 p-4
							hover:border-slate-600 transition-colors"
					>
						<div className="flex items-center justify-between">
							<div className="flex-1">
								<h3 className="text-white font-medium">{doc.fileName}</h3>
								<p className="text-sm text-slate-400 mt-1">
									Uploaded {new Date(doc.createdAt).toLocaleDateString()}
								</p>
							</div>

							<div className="ml-4 flex items-center gap-2">
								<button
									onClick={(e) => handleReprocess(e, doc.id)}
									disabled={reprocessMutation.isPending}
									className="px-3 py-1 text-xs font-medium rounded-full border
										border-slate-600 bg-slate-700 text-slate-300
										hover:bg-slate-600 hover:text-white
										disabled:opacity-50 disabled:cursor-not-allowed
										transition-colors"
									title="Reprocess document"
								>
									{reprocessMutation.isPending ? "..." : "Restart"}
								</button>
								<StatusBadge status={doc.processingStatus} />
							</div>
						</div>

						{doc.processingError && (
							<p className="text-sm text-red-400 mt-2">
								Error: {doc.processingError}
							</p>
						)}
					</Link>
				))}
			</div>

			{totalPages > 1 && (
				<div className="flex items-center justify-between pt-2">
					<p className="text-sm text-slate-400">
						Showing {page * PAGE_SIZE + 1}-{Math.min((page + 1) * PAGE_SIZE, total)} of {total}
					</p>
					<div className="flex gap-2">
						<button
							onClick={() => setPage((p) => p - 1)}
							disabled={!hasPrev}
							className="px-3 py-1 text-sm font-medium rounded border
								border-slate-600 bg-slate-700 text-slate-300
								hover:bg-slate-600 hover:text-white
								disabled:opacity-50 disabled:cursor-not-allowed
								transition-colors"
						>
							Previous
						</button>
						<button
							onClick={() => setPage((p) => p + 1)}
							disabled={!hasNext}
							className="px-3 py-1 text-sm font-medium rounded border
								border-slate-600 bg-slate-700 text-slate-300
								hover:bg-slate-600 hover:text-white
								disabled:opacity-50 disabled:cursor-not-allowed
								transition-colors"
						>
							Next
						</button>
					</div>
				</div>
			)}
		</div>
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
				styles[status as keyof typeof styles]
			}`}
		>
			{status}
		</span>
	);
}
