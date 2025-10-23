# COMA_API_PROMPTS (Contracts + REST + OpenAPI)

## P2B.1 Contracts (Zod)

- Tạo `lib/api/contracts/*.ts` cho Project/Member/DailyLog/Media/Transaction/Report.
- Quy ước: <Name>Input, <Name>Response; camelCase; error: { error, code }.

## P2B.2 REST Routes

- `/api/projects`, `/api/projects/[id]`, `/api/projects/[id]/members`, `/api/projects/[id]/daily-logs`, `/api/projects/[id]/media`, `/api/projects/[id]/transactions`, `/api/projects/[id]/reports`.
- Validate zod, guard project access, pagination tiêu chuẩn.

## P2B.3 OpenAPI nội bộ

- zod-to-openapi → `/api/docs` (guard OWNER/ADMIN), script `pnpm api:spec`.

## P2B.4 Error & Logging Standard

- `AppError(code,status)`; handler wrapper cho mọi route; log tối thiểu, không rò PII.
