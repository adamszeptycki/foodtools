ALTER TABLE "machine_fixes" ADD COLUMN "searchable_text" text;--> statement-breakpoint
ALTER TABLE "machine_fixes" ADD COLUMN "summarized_searchable_text" text;--> statement-breakpoint
ALTER TABLE "machine_fixes" ADD COLUMN "embedding_summarized" vector(1536);--> statement-breakpoint
ALTER TABLE "machine_fixes" ADD COLUMN "search_vector" "tsvector";--> statement-breakpoint

-- HNSW index for summarized embedding (vector cosine similarity)
CREATE INDEX "machine_fixes_embedding_summarized_idx" ON "machine_fixes" USING hnsw ("embedding_summarized" vector_cosine_ops);--> statement-breakpoint

-- GIN index for full-text search
CREATE INDEX "machine_fixes_search_vector_idx" ON "machine_fixes" USING gin ("search_vector");