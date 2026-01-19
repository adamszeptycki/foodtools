"use client";

import Image from "next/image";
import Link from "next/link";

export default function DashboardPage() {
	return (
		<div className="space-y-6 rounded-lg border border-slate-800 bg-slate-900/60 p-6">
			<div className="flex justify-center py-4">
				<Image
					src="/foodtools-logo.png"
					alt="FoodTools Logo"
					width={300}
					height={80}
					className="object-contain"
				/>
			</div>

			<h1 className="text-2xl font-semibold text-white">Dashboard</h1>

			<div className="space-y-4">
				<p className="text-slate-300">
					Welcome to FoodTools - your central hub for managing and searching
					service reports. Upload documents, search through your reports, and
					track your service history all in one place.
				</p>

				<ul className="list-inside list-disc space-y-1 text-slate-400">
					<li>Search through all your service reports quickly</li>
					<li>Upload and organize new documents</li>
					<li>View statistics and insights</li>
				</ul>
			</div>

			<div className="flex items-center gap-4 pt-2">
				<Link
					href="/search"
					className="rounded bg-blue-600 px-6 py-2.5 font-medium text-white transition-colors hover:bg-blue-700"
				>
					Start Search
				</Link>
				<Link
					href="/documents"
					className="rounded border border-slate-600 px-4 py-2 text-sm text-slate-300 transition-colors hover:bg-slate-800"
				>
					Upload Documents
				</Link>
			</div>
		</div>
	);
}
