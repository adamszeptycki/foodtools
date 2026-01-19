export const Stage = {
	ADAM: "adam",
	JUSTME: "justme",
	PROD: "production",
	DEV: "dev",
} as const;

export type StageType = (typeof Stage)[keyof typeof Stage];
