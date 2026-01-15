import { resolve } from "node:path";
import { defineConfig } from "vite";

export default defineConfig({
	build: {
		lib: {
			entry: resolve(__dirname, "src/index.ts"),
			name: "@foodtools/types",
			fileName: "index",
		},
		rollupOptions: {
			external: ["zod"],
		},
	},
});
