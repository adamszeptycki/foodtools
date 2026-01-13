import Link from "next/link";

export default function Home() {
	return (
		<div className="flex min-h-screen flex-col items-center justify-center px-6">
			<div className="flex max-w-2xl flex-col items-center gap-8 text-center">
				<div className="flex flex-col gap-4">
					<h1 className="text-5xl font-bold text-white">FoodTools</h1>
					<p className="text-xl text-slate-300">
						Service document management for commercial kitchen equipment
					</p>
				</div>

				<div className="flex flex-col gap-3 text-slate-400">
					<p>Upload service reports, extract repair data automatically,</p>
					<p>and search similar fixes across your entire history.</p>
				</div>

				<Link
					href="/dashboard"
					className="mt-4 rounded-lg bg-blue-600 px-8 py-3 text-lg font-medium text-white transition-colors hover:bg-blue-700"
				>
					Go to Dashboard
				</Link>

				<div className="mt-8 flex gap-8 text-sm text-slate-500">
					<div className="flex items-center gap-2">
						<span className="h-2 w-2 rounded-full bg-green-500" />
						Document Upload
					</div>
					<div className="flex items-center gap-2">
						<span className="h-2 w-2 rounded-full bg-green-500" />
						AI Extraction
					</div>
					<div className="flex items-center gap-2">
						<span className="h-2 w-2 rounded-full bg-green-500" />
						Semantic Search
					</div>
				</div>
			</div>
		</div>
	);
}
