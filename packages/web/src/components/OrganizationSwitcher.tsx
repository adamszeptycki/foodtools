"use client";

import { trpc } from "@foodtools/core-web/src/trpc/client";
import { useRouter } from "next/navigation";
import Link from "next/link";
import { useState, useRef, useEffect } from "react";

const DEFAULT_LOGO = "https://media.licdn.com/dms/image/v2/C560BAQHIvtmXaxi_Yw/company-logo_100_100/company-logo_100_100/0/1678043468851/foodtools_logo?e=1769644800&v=beta&t=zFusmoLvi3TtTq8y0FCvmB9PhdGAO4ohuT5ON6OdlSI";

export function OrganizationSwitcher() {
	const router = useRouter();
	const [isOpen, setIsOpen] = useState(false);
	const dropdownRef = useRef<HTMLDivElement>(null);
	const utils = trpc.useUtils();

	const { data: user } = trpc.user.me.useQuery();
	const { data: orgData } = trpc.organization.listUserOrganizations.useQuery();
	const setCurrentOrg = trpc.organization.setCurrentOrganization.useMutation({
		onSuccess: () => {
			// Invalidate all queries to refetch with new org context
			utils.invalidate();
			// Reload to ensure all data is fresh
			window.location.reload();
		},
	});

	// Close dropdown when clicking outside
	useEffect(() => {
		function handleClickOutside(event: MouseEvent) {
			if (dropdownRef.current && !dropdownRef.current.contains(event.target as Node)) {
				setIsOpen(false);
			}
		}
		document.addEventListener("mousedown", handleClickOutside);
		return () => document.removeEventListener("mousedown", handleClickOutside);
	}, []);

	const handleSwitchOrg = async (orgId: string) => {
		if (orgId === user?.organization?.id) {
			setIsOpen(false);
			return;
		}
		await setCurrentOrg.mutateAsync({ organizationId: orgId });
	};

	const currentOrgName = user?.organization?.name || "Select Organization";
	const currentOrgLogo = user?.organization?.logo || DEFAULT_LOGO;
	const organizations = orgData?.orgsList || [];
	const hasMultipleOrgs = organizations.length > 1;

	return (
		<div className="relative" ref={dropdownRef}>
			<button
				onClick={() => setIsOpen(!isOpen)}
				className="flex w-full items-center justify-between rounded-lg bg-slate-800 px-4 py-3 text-left text-white transition-colors hover:bg-slate-700"
			>
				<div className="flex items-center gap-3">
					<img
						src={currentOrgLogo}
						alt={currentOrgName}
						className="h-8 w-8 rounded-lg object-cover"
					/>
					<div>
						<p className="text-sm font-medium">{currentOrgName}</p>
						{hasMultipleOrgs && (
							<p className="text-xs text-slate-400">{organizations.length} organizations</p>
						)}
					</div>
				</div>
				<svg
					className={`h-5 w-5 text-slate-400 transition-transform ${isOpen ? "rotate-180" : ""}`}
					fill="none"
					viewBox="0 0 24 24"
					stroke="currentColor"
				>
					<path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
				</svg>
			</button>

			{isOpen && (
				<div className="absolute left-0 right-0 top-full z-50 mt-2 rounded-lg border border-slate-700 bg-slate-800 py-2 shadow-xl">
					{/* Settings Link */}
					<Link
						href="/dashboard/settings"
						className="flex items-center gap-2 px-4 py-2 text-sm text-slate-300 hover:bg-slate-700"
						onClick={() => setIsOpen(false)}
					>
						<svg className="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
							<path
								strokeLinecap="round"
								strokeLinejoin="round"
								strokeWidth={2}
								d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"
							/>
							<path
								strokeLinecap="round"
								strokeLinejoin="round"
								strokeWidth={2}
								d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"
							/>
						</svg>
						Settings
					</Link>

					{/* Divider */}
					{hasMultipleOrgs && <div className="my-2 border-t border-slate-700" />}

					{/* Organization List */}
					{hasMultipleOrgs && (
						<div className="max-h-48 overflow-y-auto">
							<p className="px-4 py-1 text-xs font-medium uppercase text-slate-500">
								Switch Organization
							</p>
							{organizations.map((org) => (
								<button
									key={org.id}
									onClick={() => handleSwitchOrg(org.id)}
									disabled={setCurrentOrg.isPending}
									className="flex w-full items-center justify-between px-4 py-2 text-sm text-slate-300 hover:bg-slate-700 disabled:opacity-50"
								>
									<div className="flex items-center gap-2">
										<img
											src={org.logo || DEFAULT_LOGO}
											alt={org.name || "Organization"}
											className="h-6 w-6 rounded object-cover"
										/>
										<span>{org.name}</span>
									</div>
									{org.id === user?.organization?.id && (
										<svg
											className="h-4 w-4 text-green-500"
											fill="none"
											viewBox="0 0 24 24"
											stroke="currentColor"
										>
											<path
												strokeLinecap="round"
												strokeLinejoin="round"
												strokeWidth={2}
												d="M5 13l4 4L19 7"
											/>
										</svg>
									)}
								</button>
							))}
						</div>
					)}

					{/* Divider */}
					<div className="my-2 border-t border-slate-700" />

					{/* Create New Organization */}
					<Link
						href="/onboarding/create-organization"
						className="flex items-center gap-2 px-4 py-2 text-sm text-slate-300 hover:bg-slate-700"
						onClick={() => setIsOpen(false)}
					>
						<svg className="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
							<path
								strokeLinecap="round"
								strokeLinejoin="round"
								strokeWidth={2}
								d="M12 4v16m8-8H4"
							/>
						</svg>
						Create new organization
					</Link>
				</div>
			)}
		</div>
	);
}
