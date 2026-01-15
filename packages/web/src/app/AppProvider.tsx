"use client";

import TrpcProvider from "@foodtools/core-web/src/trpc/Provider";
import type { ReactNode } from "react";

const AppProvider = ({ children }: { children: ReactNode }) => {
	return <TrpcProvider>{children}</TrpcProvider>;
};

export default AppProvider;
