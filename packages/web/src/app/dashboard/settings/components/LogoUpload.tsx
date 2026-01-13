"use client";

import { useState, useCallback } from "react";
import { useDropzone } from "react-dropzone";
import { trpc } from "@foodtools/core-web/src/trpc/client";

const MAX_FILE_SIZE = 5 * 1024 * 1024; // 5MB
const DEFAULT_LOGO = "https://media.licdn.com/dms/image/v2/C560BAQHIvtmXaxi_Yw/company-logo_100_100/company-logo_100_100/0/1678043468851/foodtools_logo?e=1769644800&v=beta&t=zFusmoLvi3TtTq8y0FCvmB9PhdGAO4ohuT5ON6OdlSI";

interface LogoUploadProps {
	currentLogo?: string | null;
}

export function LogoUpload({ currentLogo }: LogoUploadProps) {
	const [uploading, setUploading] = useState(false);
	const [error, setError] = useState<string | null>(null);
	const [previewUrl, setPreviewUrl] = useState<string | null>(currentLogo || DEFAULT_LOGO);

	const initiateLogoUploadMutation = trpc.organization.initiateLogoUpload.useMutation();
	const updateOrganizationMutation = trpc.organization.update.useMutation();
	const utils = trpc.useUtils();

	const onDrop = useCallback(async (acceptedFiles: File[]) => {
		const file = acceptedFiles[0];
		if (!file) return;

		setError(null);
		setUploading(true);

		try {
			// Get presigned URL
			const { uploadUrl, logoUrl } = await initiateLogoUploadMutation.mutateAsync({
				fileName: file.name,
				fileSize: file.size,
				mimeType: file.type,
			});

			// Upload to S3
			const uploadResponse = await fetch(uploadUrl, {
				method: "PUT",
				body: file,
				headers: {
					"Content-Type": file.type,
				},
			});

			if (!uploadResponse.ok) {
				throw new Error("Failed to upload logo to S3");
			}

			// Update organization with new logo URL
			await updateOrganizationMutation.mutateAsync({
				logo: logoUrl,
			});

			// Update preview
			setPreviewUrl(logoUrl);

			// Invalidate queries
			utils.organization.getCurrent.invalidate();
			utils.organization.listUserOrganizations.invalidate();
		} catch (err) {
			setError(err instanceof Error ? err.message : "Upload failed");
		} finally {
			setUploading(false);
		}
	}, [initiateLogoUploadMutation, updateOrganizationMutation, utils]);

	const { getRootProps, getInputProps, isDragActive } = useDropzone({
		onDrop,
		accept: {
			"image/png": [".png"],
			"image/jpeg": [".jpg", ".jpeg"],
			"image/webp": [".webp"],
		},
		maxSize: MAX_FILE_SIZE,
		multiple: false,
		disabled: uploading,
	});

	return (
		<div className="rounded-lg border border-slate-700 bg-slate-800 p-6">
			<h2 className="text-xl font-semibold text-white mb-4">
				Company Logo
			</h2>

			{/* Current Logo Preview */}
			{previewUrl && (
				<div className="mb-4">
					<p className="text-sm text-slate-400 mb-2">Current logo:</p>
					<img
						src={previewUrl}
						alt="Company logo"
						className="max-h-24 max-w-48 object-contain rounded border border-slate-600"
					/>
				</div>
			)}

			{/* Dropzone */}
			<div
				{...getRootProps()}
				className={`
					border-2 border-dashed rounded-lg p-6 text-center cursor-pointer
					transition-colors duration-200
					${uploading ? "opacity-50 cursor-not-allowed" : ""}
					${
						isDragActive
							? "border-blue-500 bg-blue-500/10"
							: "border-slate-600 hover:border-slate-500 hover:bg-slate-700/50"
					}
				`}
			>
				<input {...getInputProps()} />
				<div className="text-slate-400">
					{uploading ? (
						<p className="font-medium">Uploading...</p>
					) : isDragActive ? (
						<p className="text-blue-400 font-medium">Drop the image here...</p>
					) : (
						<>
							<p className="font-medium">
								Drag & drop a logo image here, or click to browse
							</p>
							<p className="text-sm mt-1">PNG, JPG, or WebP (max 5MB)</p>
						</>
					)}
				</div>
			</div>

			{error && (
				<p className="mt-3 text-sm text-red-400">{error}</p>
			)}
		</div>
	);
}
