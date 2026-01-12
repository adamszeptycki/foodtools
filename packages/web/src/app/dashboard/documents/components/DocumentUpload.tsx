"use client";

import { useState, useCallback } from "react";
import { trpc } from "@starter/core-web/src/trpc/client";

export function DocumentUpload() {
	const [file, setFile] = useState<File | null>(null);
	const [uploading, setUploading] = useState(false);
	const [error, setError] = useState<string | null>(null);

	const initiateUploadMutation = trpc.serviceDocuments.initiateUpload.useMutation();
	const confirmUploadMutation = trpc.serviceDocuments.confirmUpload.useMutation();
	const utils = trpc.useUtils();

	const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
		const selectedFile = e.target.files?.[0];
		if (selectedFile) {
			if (selectedFile.type !== "application/pdf") {
				setError("Only PDF files are allowed");
				return;
			}
			if (selectedFile.size > 10 * 1024 * 1024) {
				setError("File size must be less than 10MB");
				return;
			}
			setFile(selectedFile);
			setError(null);
		}
	};

	const handleUpload = async () => {
		if (!file) return;

		setUploading(true);
		setError(null);

		try {
			// Step 1: Initiate upload - get presigned URL
			const { documentId, uploadUrl } =
				await initiateUploadMutation.mutateAsync({
					fileName: file.name,
					fileSize: file.size,
					mimeType: file.type,
				});

			// Step 2: Upload file to S3 using presigned URL
			const uploadResponse = await fetch(uploadUrl, {
				method: "PUT",
				body: file,
				headers: {
					"Content-Type": file.type,
				},
			});

			if (!uploadResponse.ok) {
				throw new Error("Failed to upload file to S3");
			}

			// Step 3: Confirm upload and trigger processing
			await confirmUploadMutation.mutateAsync({ documentId });

			// Reset form
			setFile(null);

			// Invalidate queries to refresh document list
			utils.serviceDocuments.list.invalidate();
		} catch (err) {
			setError(err instanceof Error ? err.message : "Upload failed");
		} finally {
			setUploading(false);
		}
	};

	return (
		<div className="rounded-lg border border-slate-700 bg-slate-800 p-6">
			<h2 className="text-xl font-semibold text-white mb-4">
				Upload Service Document
			</h2>

			<div className="space-y-4">
				<div>
					<label
						htmlFor="file-upload"
						className="block text-sm font-medium text-slate-300 mb-2"
					>
						Select PDF file (max 10MB)
					</label>
					<input
						id="file-upload"
						type="file"
						accept="application/pdf"
						onChange={handleFileChange}
						disabled={uploading}
						className="block w-full text-sm text-slate-300
              file:mr-4 file:py-2 file:px-4
              file:rounded-md file:border-0
              file:text-sm file:font-semibold
              file:bg-blue-600 file:text-white
              hover:file:bg-blue-700
              file:cursor-pointer
              disabled:opacity-50"
					/>
				</div>

				{file && (
					<div className="text-sm text-slate-400">
						Selected: {file.name} ({(file.size / 1024 / 1024).toFixed(2)} MB)
					</div>
				)}

				{error && (
					<div className="text-sm text-red-400 bg-red-900/20 border border-red-800 rounded p-3">
						{error}
					</div>
				)}

				<button
					onClick={handleUpload}
					disabled={!file || uploading}
					className="px-4 py-2 bg-blue-600 text-white rounded-md
            hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed
            transition-colors"
				>
					{uploading ? "Uploading..." : "Upload Document"}
				</button>
			</div>
		</div>
	);
}
