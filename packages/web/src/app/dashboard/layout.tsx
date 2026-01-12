"use client";

import type { ReactNode } from "react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { AuthGuard } from "@/components/AuthGuard";
import { OrganizationSwitcher } from "@/components/OrganizationSwitcher";

type DashboardLayoutProps = {
	children: ReactNode;
};

export default function DashboardLayout({ children }: DashboardLayoutProps) {
	const pathname = usePathname();

	const isActive = (path: string) => pathname.startsWith(path);

	return (
		<AuthGuard>
			<div className="flex min-h-screen bg-slate-950">
				{/* Sidebar */}
				<aside className="w-64 bg-slate-900 border-r border-slate-800">
					<div className="p-4">
						<OrganizationSwitcher />
						<nav className="mt-6 space-y-2">
							<Link
								href="/dashboard"
								className={`block px-4 py-2 rounded-md transition-colors ${
									pathname === "/dashboard"
										? "bg-blue-600 text-white"
										: "text-slate-300 hover:bg-slate-800"
								}`}
							>
								Dashboard
							</Link>
							<Link
								href="/dashboard/documents"
								className={`block px-4 py-2 rounded-md transition-colors ${
									isActive("/dashboard/documents")
										? "bg-blue-600 text-white"
										: "text-slate-300 hover:bg-slate-800"
								}`}
							>
								Documents
							</Link>
							<Link
								href="/dashboard/search"
								className={`block px-4 py-2 rounded-md transition-colors ${
									isActive("/dashboard/search")
										? "bg-blue-600 text-white"
										: "text-slate-300 hover:bg-slate-800"
								}`}
							>
								Search Fixes
							</Link>
						</nav>
					</div>
				</aside>

				{/* Main content */}
				<main className="flex-1 p-6 overflow-auto">{children}</main>
			</div>
		</AuthGuard>
	);
}
