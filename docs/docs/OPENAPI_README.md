# OPENAPI_README

- Dùng zod-to-openapi sinh spec nội bộ.
- Endpoint nội bộ: /api/docs (guard OWNER/ADMIN).
- Script: `pnpm api:spec` -> tạo openapi.json.
- Import spec vào Postman/Insomnia để test.

> Lưu ý: tất cả route dùng `lib/api/handler.ts` để chuẩn hóa lỗi `{ error, code }`.
