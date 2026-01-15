import { z } from "zod";
import { GetChatTitleTaskSchema } from "./getChatTitle";
import { RewritePromptsForNewOrganizationTaskSchema } from "./rewritePromptsForNewOrganization";
import { NameEmbeddingTaskSchema } from "./nameEmbedding";
import { ExtractQuestionsFromDocumentTaskSchema } from "./extractQuestionsFromDocument";
import { ExtractQuestionsFromDocumentChunkTaskSchema } from "./extractQuestionsFromDocumentChunk";
import { HandleOrgDataTaskSchema } from "./handleOrgData";
import { GenerateL10DemoTaskSchema } from "./generateL10Demo";
import { GradeCallTaskSchema } from "./gradeCall";
import { HubspotSyncTaskSchema } from "./hubspotSync";
import { CallResearchTaskSchema } from "./callResearchTask";

export const GeneralSmallTaskQueueRecordSchema = z.discriminatedUnion("task_type", [
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
]);

export type GeneralSmallTaskQueueMessage = z.infer<typeof GeneralSmallTaskQueueRecordSchema>;

export type GeneralSmallTaskQueuePushMessageToQueueArgs = {
    message: GeneralSmallTaskQueueMessage;
    queue: 'SmallTaskQueue'
}

