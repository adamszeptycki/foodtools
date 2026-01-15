import SignUpForm from "./SignUpForm";

export default async function SignUpPage({
	searchParams,
}: {
	searchParams: Promise<{ email?: string; invitationId?: string }>;
}) {
	const params = await searchParams;
	const defaultEmail = params.email || "";
	const invitationId = params.invitationId || "";

	return <SignUpForm defaultEmail={defaultEmail} invitationId={invitationId} />;
}
