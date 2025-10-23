# COMA – Full Development Pack (Lean SaaS + Guardrails + API Contracts)

> Bộ tài liệu “sâu chuỗi toàn bộ” cho COMA, tương thích Cursor AI (“con lợn”) và boilerplate ixartz.
> Mục tiêu: **nhanh, chắc, nhất quán, testable**.

## 📚 Mục lục

- Product & Roadmap
  - [COMA_PRODUCT_BRIEF.md](COMA_PRODUCT_BRIEF.md)
  - [COMA_ROADMAP.md](COMA_ROADMAP.md)
- Quy trình & Chuẩn vận hành
  - [SYSTEM_PROMPT_COMA.md](SYSTEM_PROMPT_COMA.md)
  - [PROJECT_RULES.md](PROJECT_RULES.md)
  - [CODING_STANDARDS.md](CODING_STANDARDS.md)
  - [CI_CD_CHECKLIST.md](CI_CD_CHECKLIST.md)
  - [CURSOR_GUARDRAILS.md](CURSOR_GUARDRAILS.md)
  - [DB_MIGRATION_POLICY.md](DB_MIGRATION_POLICY.md)
  - [PR_CHECKLIST.md](PR_CHECKLIST.md)
  - [COMA_RUNBOOK.md](COMA_RUNBOOK.md)
- Prompt theo Phase & API
  - [COMA_PHASE_PROMPTS.md](COMA_PHASE_PROMPTS.md)
  - [COMA_API_PROMPTS.md](COMA_API_PROMPTS.md)
- Mẫu Sprint/Changelog/Postmortem
  - [COMA_SPRINT_TEMPLATE.md](COMA_SPRINT_TEMPLATE.md)
  - [COMA_CHANGELOG_TEMPLATE.md](COMA_CHANGELOG_TEMPLATE.md)
  - [COMA_POSTMORTEM_TEMPLATE.md](COMA_POSTMORTEM_TEMPLATE.md)
- Môi trường & OpenAPI
  - [ENV_SETUP_WSL.md](ENV_SETUP_WSL.md)
  - [OPENAPI_README.md](OPENAPI_README.md)
  - [DATA_TESTIDS_GUIDE.md](DATA_TESTIDS_GUIDE.md)

## 🧩 Contracts (Zod)

- Thư mục: `lib/api/contracts/` – điểm sự thật duy nhất cho input/output API.
- Sử dụng trong server actions & route handlers.
- Có thể sinh OpenAPI nội bộ.

## 💡 Cách dùng nhanh

1. Giải nén vào root repo `coma/` (hoặc copy `docs/` và `lib/` vào project).
2. Ghim `docs/SYSTEM_PROMPT_COMA.md` + `docs/PROJECT_RULES.md` + `docs/CODING_STANDARDS.md` vào Cursor Context.
3. Triển khai theo `docs/COMA_PHASE_PROMPTS.md` (P1 → …).
4. Khi viết API/FE, dựa vào `lib/api/contracts/*.ts`.
5. Thay đổi lớn → tạo `docs/ADR-xxx.md` theo `docs/ADR_TEMPLATE.md`.

## ✅ Triết lý

- **Lean trước – Formal sau.**
- **Contracts trước – Code sau.**
- **Mọi thay đổi đều test & quan sát được.**
