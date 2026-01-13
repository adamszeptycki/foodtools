"use client";

import { trpc } from "@foodtools/core-web/src/trpc/client";
import { LogoUpload } from "./components/LogoUpload";

export default function SettingsPage() {
	const { data: organization, isLoading } = trpc.organization.getCurrent.useQuery();

	if (isLoading) {
		return (
			<div className="space-y-6">
				<h1 className="text-2xl font-semibold text-white">Settings</h1>
				<div className="text-slate-400">Loading...</div>
			</div>
		);
	}

	if (!organization) {
		return (
			<div className="space-y-6">
				<h1 className="text-2xl font-semibold text-white">Settings</h1>
				<div className="text-slate-400">No organization found</div>
			</div>
		);
	}

	return (
		<div className="space-y-6">
			<h1 className="text-2xl font-semibold text-white">Settings</h1>

			<div className="rounded-lg border border-slate-700 bg-slate-800 p-6">
				<h2 className="text-xl font-semibold text-white mb-4">
					Organization
				</h2>
				<div className="space-y-4">
					<div>
						<span className="text-slate-400 text-sm">Name:</span>
						<p className="text-white">{organization.name}</p>
					</div>
					{organization.slug && (
						<div>
							<span className="text-slate-400 text-sm">Slug:</span>
							<p className="text-white">{organization.slug}</p>
						</div>
					)}
				</div>
			</div>

			<LogoUpload currentLogo={organization.logo} />
		</div>
	);
}
