'use client';

import type { ReactNode } from "react";
import TrpcProvider from "@foodtools/core-web/src/trpc/Provider";

const AppProvider = ({ children }: { children: ReactNode }) => {
	return (
		<TrpcProvider>
			{children}
		</TrpcProvider>
	);
};

export default AppProvider;
