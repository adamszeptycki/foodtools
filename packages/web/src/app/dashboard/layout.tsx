"use client";

import type { ReactNode } from "react";
import Image from "next/image";
import Link from "next/link";
import { usePathname } from "next/navigation";

type DashboardLayoutProps = {
	children: ReactNode;
};

export default function DashboardLayout({ children }: DashboardLayoutProps) {
	const pathname = usePathname();

	const isActive = (path: string) => pathname.startsWith(path);

	return (
		<div className="flex min-h-screen">
			{/* Sidebar */}
			<aside className="w-64 bg-slate-900 border-r border-slate-800">
				<div className="p-6">
					<div className="mb-6">
						<Image
							src="/logo.jpeg"
							alt="Company Logo"
							width={48}
							height={48}
							className="mb-2"
						/>
						<h2 className="text-xl font-bold text-white">
							Machine Service
						</h2>
					</div>
					<nav className="space-y-2">
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
			<main className="flex-1 p-6">{children}</main>
		</div>
	);
}
