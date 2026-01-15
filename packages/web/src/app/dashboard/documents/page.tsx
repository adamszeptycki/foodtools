import { DocumentList } from "./components/DocumentList";
import { DocumentUpload } from "./components/DocumentUpload";

export default function DocumentsPage() {
	return (
		<div className="space-y-6">
			<h1 className="text-2xl font-semibold text-white">Service Documents</h1>

			<DocumentUpload />

			<div className="rounded-lg border border-slate-800 bg-slate-900/60 p-6">
				<h2 className="text-xl font-semibold text-white mb-4">
					Uploaded Documents
				</h2>
				<DocumentList />
			</div>
		</div>
	);
}
