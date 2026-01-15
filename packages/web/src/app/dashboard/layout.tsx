"use client";

import { useState, type ReactNode } from "react";
import Image from "next/image";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { AuthGuard } from "@/components/AuthGuard";
import { OrganizationSwitcher } from "@/components/OrganizationSwitcher";

type DashboardLayoutProps = {
	children: ReactNode;
};

export default function DashboardLayout({ children }: DashboardLayoutProps) {
	const pathname = usePathname();
	const [sidebarOpen, setSidebarOpen] = useState(false);

	const isActive = (path: string) => pathname.startsWith(path);

	return (
		<AuthGuard>
			<div className="flex min-h-screen bg-slate-950 relative">
				{/* Logo - top right corner */}
				<div className="absolute top-4 right-4 z-10">
					<Image
						src="/logo.jpeg"
						alt="Logo"
						width={48}
						height={48}
						className="rounded-lg"
					/>
				</div>

				{/* Sidebar */}
				<aside
					className={`
						${sidebarOpen ? "w-64" : "w-0"}
						bg-slate-900 border-r border-slate-800 overflow-hidden transition-all duration-300
					`}
				>
					<div className="w-64 p-4">
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
								Service Reports
							</Link>
							<Link
								href="/dashboard/search"
								className={`block px-4 py-2 rounded-md transition-colors ${
									isActive("/dashboard/search")
										? "bg-blue-600 text-white"
										: "text-slate-300 hover:bg-slate-800"
								}`}
							>
								Search Service Reports
							</Link>
							<Link
								href="/dashboard/statistics"
								className={`block px-4 py-2 rounded-md transition-colors ${
									isActive("/dashboard/statistics")
										? "bg-blue-600 text-white"
										: "text-slate-300 hover:bg-slate-800"
								}`}
							>
								Statistics
							</Link>
							<Link
								href="/dashboard/settings"
								className={`block px-4 py-2 rounded-md transition-colors ${
									isActive("/dashboard/settings")
										? "bg-blue-600 text-white"
										: "text-slate-300 hover:bg-slate-800"
								}`}
							>
								Settings
							</Link>
						</nav>
					</div>
				</aside>

				{/* Main content */}
				<main className="flex-1 p-6 overflow-auto hide-scrollbar">
					{/* Menu toggle button */}
					<button
						onClick={() => setSidebarOpen(!sidebarOpen)}
						className="mb-4 p-2 rounded-md text-slate-400 hover:text-white hover:bg-slate-800 transition-colors"
						aria-label={sidebarOpen ? "Close menu" : "Open menu"}
					>
						<svg
							className="w-6 h-6"
							fill="none"
							stroke="currentColor"
							viewBox="0 0 24 24"
						>
							{sidebarOpen ? (
								<path
									strokeLinecap="round"
									strokeLinejoin="round"
									strokeWidth={2}
									d="M6 18L18 6M6 6l12 12"
								/>
							) : (
								<path
									strokeLinecap="round"
									strokeLinejoin="round"
									strokeWidth={2}
									d="M4 6h16M4 12h16M4 18h16"
								/>
							)}
						</svg>
					</button>
					{children}
				</main>
			</div>
		</AuthGuard>
	);
}
