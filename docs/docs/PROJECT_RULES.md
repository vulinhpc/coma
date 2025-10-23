# 📏 PROJECT RULES — COMA

- OS: Windows 10 + WSL Ubuntu 22.04, Node 20, pnpm 9.
- DB: Postgres 16 + Drizzle; Auth: Clerk; Media: Cloudinary; Deploy: Vercel.
- TS strict; Không đổi boilerplate ixartz nếu không có ADR.
- Secrets qua Vercel Env; Không thêm UI libs ngoài Shadcn nếu chưa duyệt.
- Quyền: OWNER, ADMIN, PM, SITE, ACCOUNTANT.
- API & server actions luôn guard theo project_id membership.
