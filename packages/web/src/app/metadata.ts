import type { Metadata } from "next";

export const metadata: Metadata = {
	metadataBase: new URL(
		process.env.NEXT_PUBLIC_BASE_URL || "http://localhost:3000",
	),
	title: "FoodTools - Service Report Search",
	description:
		"Search and analyze service reports for food service equipment. Find maintenance history, repair records, and equipment issues instantly with AI-powered search.",
	keywords:
		"service reports, food service equipment, maintenance records, repair history, equipment search, AI search",
	openGraph: {
		title: "FoodTools - Service Report Search",
		description:
			"Search and analyze service reports for food service equipment. Find maintenance history, repair records, and equipment issues instantly with AI-powered search.",
		type: "website",
		url: "https://Lucidiant-ai.com",
		images: [
			{
				url: "/og-image.png",
				width: 1200,
				height: 630,
				alt: "FoodTools",
			},
		],
	},
	twitter: {
		card: "summary_large_image",
		title: "FoodTools - Service Report Search",
		description:
			"Search and analyze service reports for food service equipment. Find maintenance history, repair records, and equipment issues instantly with AI-powered search.",
		images: ["/og-image.png"],
	},
};
