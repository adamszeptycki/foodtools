"use client";

import { useState, useCallback } from "react";
import { useDropzone } from "react-dropzone";
import { trpc } from "@foodtools/core-web/src/trpc/client";

interface QueuedFile {
	file: File;
	id: string;
	status: "pending" | "uploading" | "completed" | "failed";
	error?: string;
}

const MAX_FILE_SIZE = 10 * 1024 * 1024; // 10MB

export function DocumentUpload() {
	const [fileQueue, setFileQueue] = useState<QueuedFile[]>([]);
	const [uploading, setUploading] = useState(false);

	const initiateUploadBatchMutation =
		trpc.serviceDocuments.initiateUploadBatch.useMutation();
	const utils = trpc.useUtils();

	const onDrop = useCallback((acceptedFiles: File[], rejectedFiles: any[]) => {
		// Handle rejected files
		const rejectionErrors = rejectedFiles.map((rejection) => {
			const error = rejection.errors[0];
			if (error.code === "file-too-large") {
				return `${rejection.file.name}: File too large (max 10MB)`;
			}
			if (error.code === "file-invalid-type") {
				return `${rejection.file.name}: Only PDF files allowed`;
			}
			return `${rejection.file.name}: ${error.message}`;
		});

		if (rejectionErrors.length > 0) {
			console.warn("Rejected files:", rejectionErrors);
		}

		// Add accepted files to queue
		const newFiles: QueuedFile[] = acceptedFiles.map((file) => ({
			file,
			id: `${file.name}-${Date.now()}-${Math.random().toString(36).slice(2)}`,
			status: "pending" as const,
		}));

		setFileQueue((prev) => [...prev, ...newFiles]);
	}, []);

	const { getRootProps, getInputProps, isDragActive } = useDropzone({
		onDrop,
		accept: {
			"application/pdf": [".pdf"],
		},
		maxSize: MAX_FILE_SIZE,
		multiple: true,
	});

	const removeFile = (id: string) => {
		setFileQueue((prev) => prev.filter((f) => f.id !== id));
	};

	const clearQueue = () => {
		setFileQueue((prev) => prev.filter((f) => f.status === "uploading"));
	};

	const updateFileStatus = (
		id: string,
		status: QueuedFile["status"],
		error?: string
	) => {
		setFileQueue((prev) =>
			prev.map((f) => (f.id === id ? { ...f, status, error } : f))
		);
	};

	const handleUploadAll = async () => {
		const pendingFiles = fileQueue.filter((f) => f.status === "pending");
		if (pendingFiles.length === 0) return;

		setUploading(true);

		try {
			// Get presigned URLs for all files in a single request
			const uploadInfos = await initiateUploadBatchMutation.mutateAsync({
				files: pendingFiles.map((queuedFile) => ({
					fileName: queuedFile.file.name,
					fileSize: queuedFile.file.size,
					mimeType: queuedFile.file.type,
				})),
			});

			// Create a map of fileName to upload info for easy lookup
			const uploadInfoMap = new Map(
				uploadInfos.map((info) => [info.fileName, info])
			);

			// Upload all files to S3 in parallel
			const uploadPromises = pendingFiles.map(async (queuedFile) => {
				const uploadInfo = uploadInfoMap.get(queuedFile.file.name);
				if (!uploadInfo) {
					updateFileStatus(queuedFile.id, "failed", "Failed to get upload URL");
					return;
				}

				try {
					updateFileStatus(queuedFile.id, "uploading");

					// Upload to S3
					const uploadResponse = await fetch(uploadInfo.uploadUrl, {
						method: "PUT",
						body: queuedFile.file,
						headers: {
							"Content-Type": queuedFile.file.type,
						},
					});

					if (!uploadResponse.ok) {
						throw new Error("Failed to upload file to S3");
					}

					// Processing is triggered automatically by S3 event subscription
					updateFileStatus(queuedFile.id, "completed");
				} catch (err) {
					updateFileStatus(
						queuedFile.id,
						"failed",
						err instanceof Error ? err.message : "Upload failed"
					);
				}
			});

			await Promise.all(uploadPromises);
		} catch (err) {
			// If batch request fails, mark all pending files as failed
			pendingFiles.forEach((queuedFile) => {
				updateFileStatus(
					queuedFile.id,
					"failed",
					err instanceof Error ? err.message : "Failed to initiate upload"
				);
			});
		}

		// Remove completed files from queue after a short delay
		setTimeout(() => {
			setFileQueue((prev) => prev.filter((f) => f.status !== "completed"));
		}, 1500);

		// Refresh document list
		utils.serviceDocuments.list.invalidate();
		setUploading(false);
	};

	const pendingCount = fileQueue.filter((f) => f.status === "pending").length;
	const hasFiles = fileQueue.length > 0;

	return (
		<div className="rounded-lg border border-slate-700 bg-slate-800 p-6">
			<h2 className="text-xl font-semibold text-white mb-4">
				Upload Service Documents
			</h2>

			{/* Dropzone */}
			<div
				{...getRootProps()}
				className={`
					border-2 border-dashed rounded-lg p-8 text-center cursor-pointer
					transition-colors duration-200
					${
						isDragActive
							? "border-blue-500 bg-blue-500/10"
							: "border-slate-600 hover:border-slate-500 hover:bg-slate-700/50"
					}
				`}
			>
				<input {...getInputProps()} />
				<div className="text-slate-400">
					<svg
						className="mx-auto h-12 w-12 mb-3"
						stroke="currentColor"
						fill="none"
						viewBox="0 0 48 48"
						aria-hidden="true"
					>
						<path
							d="M28 8H12a4 4 0 00-4 4v20m32-12v8m0 0v8a4 4 0 01-4 4H12a4 4 0 01-4-4v-4m32-4l-3.172-3.172a4 4 0 00-5.656 0L28 28M8 32l9.172-9.172a4 4 0 015.656 0L28 28m0 0l4 4m4-24h8m-4-4v8m-12 4h.02"
							strokeWidth={2}
							strokeLinecap="round"
							strokeLinejoin="round"
						/>
					</svg>
					{isDragActive ? (
						<p className="text-blue-400 font-medium">Drop the files here...</p>
					) : (
						<>
							<p className="font-medium">
								Drag & drop PDF files here, or click to browse
							</p>
							<p className="text-sm mt-1">Max 10MB per file</p>
						</>
					)}
				</div>
			</div>

			{/* File Queue */}
			{hasFiles && (
				<div className="mt-4">
					<div className="flex items-center justify-between mb-2">
						<span className="text-sm font-medium text-slate-300">
							Queued Files ({fileQueue.length})
						</span>
						<button
							onClick={clearQueue}
							disabled={uploading}
							className="text-sm text-slate-400 hover:text-slate-300 disabled:opacity-50"
						>
							Clear All
						</button>
					</div>

					<div className="space-y-2 max-h-60 overflow-y-auto">
						{fileQueue.map((queuedFile) => (
							<div
								key={queuedFile.id}
								className={`
									flex items-center justify-between p-3 rounded-md
									${queuedFile.status === "failed" ? "bg-red-900/20 border border-red-800" : "bg-slate-700/50"}
								`}
							>
								<div className="flex items-center gap-3 min-w-0">
									{/* Status Icon */}
									<span className="flex-shrink-0">
										{queuedFile.status === "pending" && (
											<svg
												className="w-5 h-5 text-slate-400"
												fill="none"
												viewBox="0 0 24 24"
												stroke="currentColor"
											>
												<path
													strokeLinecap="round"
													strokeLinejoin="round"
													strokeWidth={2}
													d="M7 21h10a2 2 0 002-2V9.414a1 1 0 00-.293-.707l-5.414-5.414A1 1 0 0012.586 3H7a2 2 0 00-2 2v14a2 2 0 002 2z"
												/>
											</svg>
										)}
										{queuedFile.status === "uploading" && (
											<svg
												className="w-5 h-5 text-blue-400 animate-spin"
												fill="none"
												viewBox="0 0 24 24"
											>
												<circle
													className="opacity-25"
													cx="12"
													cy="12"
													r="10"
													stroke="currentColor"
													strokeWidth="4"
												/>
												<path
													className="opacity-75"
													fill="currentColor"
													d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
												/>
											</svg>
										)}
										{queuedFile.status === "completed" && (
											<svg
												className="w-5 h-5 text-green-400"
												fill="none"
												viewBox="0 0 24 24"
												stroke="currentColor"
											>
												<path
													strokeLinecap="round"
													strokeLinejoin="round"
													strokeWidth={2}
													d="M5 13l4 4L19 7"
												/>
											</svg>
										)}
										{queuedFile.status === "failed" && (
											<svg
												className="w-5 h-5 text-red-400"
												fill="none"
												viewBox="0 0 24 24"
												stroke="currentColor"
											>
												<path
													strokeLinecap="round"
													strokeLinejoin="round"
													strokeWidth={2}
													d="M6 18L18 6M6 6l12 12"
												/>
											</svg>
										)}
									</span>

									{/* File Info */}
									<div className="min-w-0">
										<p className="text-sm text-slate-200 truncate">
											{queuedFile.file.name}
										</p>
										<p className="text-xs text-slate-400">
											{(queuedFile.file.size / 1024 / 1024).toFixed(2)} MB
											{queuedFile.error && (
												<span className="text-red-400 ml-2">
													- {queuedFile.error}
												</span>
											)}
										</p>
									</div>
								</div>

								{/* Remove Button */}
								{queuedFile.status !== "uploading" && (
									<button
										onClick={() => removeFile(queuedFile.id)}
										className="flex-shrink-0 p-1 text-slate-400 hover:text-slate-300"
									>
										<svg
											className="w-4 h-4"
											fill="none"
											viewBox="0 0 24 24"
											stroke="currentColor"
										>
											<path
												strokeLinecap="round"
												strokeLinejoin="round"
												strokeWidth={2}
												d="M6 18L18 6M6 6l12 12"
											/>
										</svg>
									</button>
								)}
							</div>
						))}
					</div>
				</div>
			)}

			{/* Upload Button */}
			{hasFiles && (
				<button
					onClick={handleUploadAll}
					disabled={pendingCount === 0 || uploading}
					className="mt-4 w-full px-4 py-2 bg-blue-600 text-white rounded-md
						hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed
						transition-colors"
				>
					{uploading
						? "Uploading..."
						: `Upload ${pendingCount} File${pendingCount !== 1 ? "s" : ""}`}
				</button>
			)}
		</div>
	);
}
