"use client";

import { trpc } from "@starter/core-web/src/trpc/client";
import Link from "next/link";

export function DocumentList() {
	const { data: documents, isLoading } = trpc.serviceDocuments.list.useQuery();

	if (isLoading) {
		return <div className="text-slate-400">Loading documents...</div>;
	}

	if (!documents || documents.length === 0) {
		return (
			<div className="text-slate-400 text-center py-8">
				No documents uploaded yet
			</div>
		);
	}

	return (
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

						<div className="ml-4">
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
