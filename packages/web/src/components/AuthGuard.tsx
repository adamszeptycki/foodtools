"use client";

import { trpc } from "@foodtools/core-web/src/trpc/client";
import { useRouter } from "next/navigation";
import { useEffect } from "react";
import { LoadingSpinner } from "./LoadingSpinner";

interface AuthGuardProps {
	children: React.ReactNode;
}

export function AuthGuard({ children }: AuthGuardProps) {
	const router = useRouter();
	const {
		data: user,
		isLoading,
		error,
	} = trpc.user.me.useQuery(undefined, {
		retry: false,
	});

	useEffect(() => {
		if (isLoading) return;

		// Check if user is not authenticated
		if (error || !user) {
			router.replace("/auth/sign-in");
			return;
		}

		// Check if user needs to create/select an organization
		if (!user.organization) {
			router.replace("/onboarding/create-organization");
			return;
		}
	}, [user, isLoading, error, router]);

	// Show loading spinner while checking auth
	if (isLoading) {
		return <LoadingSpinner />;
	}

	// Don't render children while redirecting
	if (error || !user || !user.organization) {
		return <LoadingSpinner />;
	}

	return <>{children}</>;
}
