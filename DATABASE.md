# Database Setup

This project uses **Aurora Serverless v2** with **RDS Data API** for production, and local PostgreSQL for development.

## Configuration

| Environment | Database | Connection Method |
|-------------|----------|-------------------|
| Local dev | PostgreSQL (localhost:5937) | TCP via node-postgres |
| Dev/Staging (AWS) | Aurora Serverless v2 | RDS Data API |
| Production (AWS) | Aurora Serverless v2 | RDS Data API |

### Scaling Configuration

- **Dev/Staging**: 0-4 ACU with auto-pause after 5 minutes (near $0 when idle)
- **Production**: 0.5-4 ACU (always-on, ~$43/month baseline)

## Infrastructure Files

- `infra/vpc.ts` - VPC with bastion host and NAT
- `infra/database.ts` - Aurora Serverless v2 with RDS Data API

## Local Development

Local development uses a PostgreSQL database via the `DATABASE_URL` environment variable:

```bash
# Default local connection
DATABASE_URL="postgres://postgres:postgres@localhost:5937/foodtools"
```

Start your local PostgreSQL instance, then run:

```bash
pnpm dev
```

## Database Migrations

### Generate migrations from schema changes

```bash
pnpm --filter @foodtools/core db:generate:migrations
```

### Run migrations locally

```bash
pnpm --filter @foodtools/core db:migrate:local
```

### Run migrations against Aurora

1. Connect via bastion tunnel:
   ```bash
   sst tunnel --stage dev
   ```

2. In another terminal, run migrations with the Aurora connection string:
   ```bash
   DATABASE_URL="postgres://<user>:<pass>@localhost:5432/foodtools" \
     pnpm --filter @foodtools/core db:migrate:local
   ```

## Initial Aurora Setup

After first deployment, enable the pgvector extension:

```sql
CREATE EXTENSION IF NOT EXISTS vector;
```

Then run Drizzle migrations to create all tables.

## Architecture

```
┌─────────────────┐     ┌─────────────────┐
│   Next.js App   │     │  Queue Workers  │
│   (Lambda)      │     │   (Lambda)      │
└────────┬────────┘     └────────┬────────┘
         │                       │
         │  RDS Data API (HTTP)  │
         │                       │
         ▼                       ▼
┌─────────────────────────────────────────┐
│         Aurora Serverless v2            │
│         (PostgreSQL 16.4)               │
│                                         │
│  - Auto-scales 0-4 ACU                  │
│  - Auto-pauses after 5 min idle         │
│  - pgvector for embeddings              │
└─────────────────────────────────────────┘
```

## Cost Estimates

| Resource | Monthly Cost |
|----------|-------------|
| Aurora (idle, auto-paused) | ~$0 |
| Aurora (1 ACU average) | ~$87 |
| VPC NAT (EC2) | ~$4 |
| RDS Data API | ~$0.35/million requests |

## Drizzle ORM

Database connections are managed in `packages/core/src/sql/index.ts`:

- **Local**: Uses `drizzle-orm/node-postgres` with connection pooling
- **AWS**: Uses `drizzle-orm/aws-data-api/pg` with RDS Data API

Schema files are in `packages/core/src/sql/schema/`.
