# 🧭 COMA_PHASE_PROMPTS_DETAIL.md

## 🎯 Mục tiêu
Bộ prompt chi tiết giúp Cursor AI ("con lợn") thực hiện toàn bộ quy trình phát triển COMA theo đúng docs, đúng chuẩn Lean SaaS.  
Mỗi phase được tách riêng, có Context – Goals – Steps – Constraints – Verification – Reporting.

Cursor phải:
1. Đọc kỹ các file hệ thống (`SYSTEM_PROMPT_COMA.md`, `PROJECT_RULES.md`, `CODING_STANDARDS.md`, `COMA_API_PROMPTS.md`, `lib/api/contracts/`).
2. Lập kế hoạch trước khi code (nêu file tạo/sửa).
3. Thực thi tuần tự từng bước, test kỹ sau mỗi bước.
4. Báo cáo kết quả, ghi log vào `CHANGELOG.md` hoặc tạo `ADR-xxx.md` nếu có thay đổi.

---

## 🧱 PHASE 1 – FOUNDATION

### Phase 1.1 – Boilerplate & Environment Setup
**Context:** Khởi tạo COMA từ ixartz SaaS-Boilerplate, đảm bảo chạy được trên WSL Ubuntu và Vercel.

**Goals:**
- Clone boilerplate → repo `coma`.
- Thiết lập lint, prettier, tsconfig, editorconfig.
- Build và dev thành công.

**Steps:**
1. Kiểm tra môi trường (Node 20, pnpm 9, Postgres 16).
2. Áp dụng cấu hình code quality (ESLint + Prettier + EditorConfig + TSConfig).
3. Chạy `pnpm install`, `pnpm lint`, `pnpm typecheck`, `pnpm dev`.
4. Fix lỗi trước khi báo thành công.

**Constraints:**
- Không thay đổi cấu trúc boilerplate.
- Theo `CODING_STANDARDS.md` và `PROJECT_RULES.md`.

**Verification:**
- App chạy tại `localhost:3000`.
- Lint/typecheck pass.

**Reporting:**
```
## [Phase 1.1] Foundation Setup
- Config lint, prettier, tsconfig, editorconfig hoàn tất.
- Build + dev OK.
```

---

### Phase 1.2 – Database Schema & Migrations
**Context:** Thiết kế schema cho các modules chính (Projects, Members, Logs, Media, Transactions, Reports).

**Goals:**
- Tạo file `db/schema.ts`.
- Sinh migration với drizzle-kit.
- Kiểm tra bằng Drizzle Studio.

**Steps:**
1. Đọc `COMA_PRODUCT_BRIEF.md`.
2. Định nghĩa bảng (id uuid, created_at, created_by).
3. Sinh migration → `pnpm db:generate`.
4. Chạy `pnpm db:migrate`.
5. Seed demo (`scripts/seed.ts`).

**Constraints:**
- Tên bảng snake_case.
- Có project_id trong bảng con.

**Verification:**
- Migration chạy OK.
- Drizzle Studio hiển thị schema.
- Seed chạy OK.

**Reporting:**
```
## [Phase 1.2] Database Schema
- Created projects, members, logs, media, transactions, reports.
```

---

## ⚙️ PHASE 2 – CORE MODULES (CRUD + SERVER ACTIONS)

### Phase 2.1 – Projects & Members
**Goals:**
- CRUD Projects.
- CRUD Members trong 1 project.
- Server actions: `createProject`, `updateProject`, `deleteProject`.

**Steps:**
1. UI Projects page + form.
2. Validate bằng `ProjectInput`.
3. Guard quyền OWNER/ADMIN.
4. Test CRUD đầy đủ.

**Verification:**
- CRUD hoạt động.
- Type-safe E2E.

**Reporting:**
```
## [Phase 2.1] Projects + Members
- CRUD Projects + Members hoàn tất.
```

---

### Phase 2.2 – Daily Logs & Media
**Goals:**
- CRUD Daily Logs.
- Upload media (Cloudinary signed).

**Steps:**
1. Form tạo nhật ký (zod validate).
2. Upload ảnh → Cloudinary → save public_id.
3. Liên kết ảnh với log.

**Verification:**
- Upload OK, logs hiển thị ảnh.

---

### Phase 2.3 – Transactions
**Goals:** Quản lý thu/chi, CRUD Transactions.

**Steps:**
1. Form thêm chi phí/thu nhập.
2. Validate theo `TransactionInput`.
3. Tổng hợp bằng Drizzle query.

---

## ⚙️ PHASE 2B – API LAYER (REST + OPENAPI)

**Context:** Chuẩn hóa contract & route cho API.

**Goals:**
- Tạo REST routes `/api/...`.
- Validate bằng Zod contracts.
- Tạo OpenAPI spec nội bộ.

**Steps:**
1. Dựa theo `COMA_API_PROMPTS.md`.
2. Dùng `withApiHandler()` và `AppError`.
3. Sinh `/api/docs` (zod-to-openapi).

**Verification:**
- Tất cả routes trả `{ error, code }` khi lỗi.
- /api/docs hoạt động.

---

## 📊 PHASE 3 – DASHBOARD & REPORTS

**Goals:**
- Dashboard tổng hợp KPI (ảnh, log, chi tiêu, thu nhập).

**Steps:**
1. Tạo server action `getDashboardKPI()`.
2. Query aggregate từ DB.
3. Render KPI cards.

**Verification:**
- KPI chính xác với dữ liệu seed.

---

## 🎨 PHASE 4 – UX & E2E TESTING

**Goals:**
- Nâng cấp UX, thêm Playwright test.

**Steps:**
1. Dùng data-testid theo `DATA_TESTIDS_GUIDE.md`.
2. Tạo test CRUD Projects + Upload ảnh.

**Verification:**
- Test pass trên CI.
- Không có flaky test.

---

## 🚀 PHASE 5 – LAUNCH & RUNBOOK

**Goals:**
- Seed demo.
- Viết CHANGELOG + RUNBOOK.

**Steps:**
1. Chạy `pnpm tsx scripts/seed.ts`.
2. Tạo CHANGELOG v1.0.
3. Review Runbook + Observability.

**Verification:**
- App production chạy OK.
- Logs sạch, KPI đúng.

**Reporting:**
```
## [Phase 5] Launch
- Seed demo thành công.
- Production deploy ổn định.
```
