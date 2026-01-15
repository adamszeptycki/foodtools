import { z } from "zod";
import { CallResearchTaskSchema } from "./callResearchTask";
import { ExtractQuestionsFromDocumentTaskSchema } from "./extractQuestionsFromDocument";
import { ExtractQuestionsFromDocumentChunkTaskSchema } from "./extractQuestionsFromDocumentChunk";
import { GenerateL10DemoTaskSchema } from "./generateL10Demo";
import { GetChatTitleTaskSchema } from "./getChatTitle";
import { GradeCallTaskSchema } from "./gradeCall";
import { HandleOrgDataTaskSchema } from "./handleOrgData";
import { HubspotSyncTaskSchema } from "./hubspotSync";
import { NameEmbeddingTaskSchema } from "./nameEmbedding";
import { RewritePromptsForNewOrganizationTaskSchema } from "./rewritePromptsForNewOrganization";

export const GeneralSmallTaskQueueRecordSchema = z.discriminatedUnion(
	"task_type",
	[
		GetChatTitleTaskSchema,
		RewritePromptsForNewOrganizationTaskSchema,
		NameEmbeddingTaskSchema,
		ExtractQuestionsFromDocumentTaskSchema,
		ExtractQuestionsFromDocumentChunkTaskSchema,
		HandleOrgDataTaskSchema,
		GenerateL10DemoTaskSchema,
		GradeCallTaskSchema,
		HubspotSyncTaskSchema,
		CallResearchTaskSchema,
	],
);

export type GeneralSmallTaskQueueMessage = z.infer<
	typeof GeneralSmallTaskQueueRecordSchema
>;

export type GeneralSmallTaskQueuePushMessageToQueueArgs = {
	message: GeneralSmallTaskQueueMessage;
	queue: "SmallTaskQueue";
};
