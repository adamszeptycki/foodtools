"use client";

export function LoadingSpinner() {
	return (
		<div className="flex h-screen w-full items-center justify-center bg-slate-950">
			<div className="flex flex-col items-center gap-4">
				<div className="h-8 w-8 animate-spin rounded-full border-4 border-slate-700 border-t-blue-500" />
				<p className="text-sm text-slate-400">Loading...</p>
			</div>
		</div>
	);
}
