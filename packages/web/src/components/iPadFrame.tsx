"use client";

import { useEffect, useState } from "react";

interface IPadFrameProps {
	children: React.ReactNode;
}

function StatusBar() {
	const [time, setTime] = useState<string>("");

	useEffect(() => {
		const updateTime = () => {
			const now = new Date();
			setTime(
				now.toLocaleTimeString("en-US", {
					hour: "numeric",
					minute: "2-digit",
					hour12: true,
				})
			);
		};
		updateTime();
		const interval = setInterval(updateTime, 1000);
		return () => clearInterval(interval);
	}, []);

	return (
		<div className="status-bar flex items-center justify-between px-6 py-1.5 text-white text-sm font-medium">
			{/* Left side - Time */}
			<div className="flex items-center gap-2">
				<span>{time}</span>
			</div>

			{/* Center - Camera area (invisible spacer) */}
			<div className="w-20" />

			{/* Right side - Network, WiFi, Battery */}
			<div className="flex items-center gap-2">
				{/* Carrier */}
				<span className="text-xs">T-Mobile</span>

				{/* Signal strength bars */}
				<div className="flex items-end gap-0.5 h-3">
					<div className="w-1 h-1 bg-white rounded-sm" />
					<div className="w-1 h-1.5 bg-white rounded-sm" />
					<div className="w-1 h-2 bg-white rounded-sm" />
					<div className="w-1 h-2.5 bg-white rounded-sm" />
				</div>

				{/* WiFi icon */}
				<svg
					className="w-4 h-4"
					viewBox="0 0 24 24"
					fill="currentColor"
				>
					<path d="M12 18c1.1 0 2 .9 2 2s-.9 2-2 2-2-.9-2-2 .9-2 2-2zm-4.9-2.3l1.4 1.4C9.4 16.4 10.6 16 12 16s2.6.4 3.5 1.1l1.4-1.4C15.6 14.6 13.9 14 12 14s-3.6.6-4.9 1.7zm-2.8-2.8l1.4 1.4C7.3 13 9.5 12 12 12s4.7 1 6.3 2.3l1.4-1.4C17.7 11.1 15 10 12 10s-5.7 1.1-7.7 2.9zM1.4 10l1.4 1.4C5.1 9.2 8.4 8 12 8s6.9 1.2 9.2 3.4l1.4-1.4C19.8 7.5 16.1 6 12 6S4.2 7.5 1.4 10z" />
				</svg>

				{/* Battery */}
				<div className="flex items-center gap-0.5">
					<div className="w-6 h-3 border border-white rounded-sm relative">
						<div className="absolute inset-0.5 bg-green-500 rounded-sm" style={{ width: "85%" }} />
					</div>
					<div className="w-0.5 h-1.5 bg-white rounded-r-sm" />
				</div>
			</div>
		</div>
	);
}

export function IPadFrame({ children }: IPadFrameProps) {
	const [scale, setScale] = useState(1);

	useEffect(() => {
		const calculateScale = () => {
			const viewportWidth = window.innerWidth;
			const viewportHeight = window.innerHeight;
			const iPadWidth = 834;
			const iPadHeight = 1194;
			const padding = 40;

			const scaleX = (viewportWidth - padding) / iPadWidth;
			const scaleY = (viewportHeight - padding) / iPadHeight;
			const newScale = Math.min(scaleX, scaleY, 1);

			setScale(newScale);
		};

		calculateScale();
		window.addEventListener("resize", calculateScale);
		return () => window.removeEventListener("resize", calculateScale);
	}, []);

	return (
		<div className="ipad-background fixed inset-0 flex items-center justify-center overflow-hidden">
			{/* iPad Device Frame */}
			<div
				className="ipad-device relative flex flex-col"
				style={{ transform: `scale(${scale})` }}
			>
				{/* Camera notch */}
				<div className="absolute top-3 left-1/2 -translate-x-1/2 z-10">
					<div className="w-2.5 h-2.5 rounded-full bg-slate-800 border border-slate-700" />
				</div>

				{/* Screen area */}
				<div className="ipad-screen flex flex-col">
					<StatusBar />
					<div className="flex-1 overflow-auto hide-scrollbar">
						{children}
					</div>
				</div>
			</div>
		</div>
	);
}
