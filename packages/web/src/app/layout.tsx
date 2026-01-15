import "./globals.css";
import { metadata } from "./metadata";
import AppProvider from "./AppProvider";
import { IPadFrame } from "@/components/iPadFrame";

export { metadata };

export default function AppLayout({
	children,
}: {
	children: React.ReactNode;
}) {
	return (
		<html lang="en" className="dark">
			<body className="font-primary min-h-screen bg-slate-950 text-slate-100 overflow-hidden">
				<AppProvider>
					<IPadFrame>
						<main className="min-h-full">{children}</main>
					</IPadFrame>
				</AppProvider>
			</body>
		</html>
	);
}
