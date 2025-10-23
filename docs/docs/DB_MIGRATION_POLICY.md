# 🗃️ DB MIGRATION POLICY — COMA

- 1 migration = 1 thay đổi độc lập; backward-compatible trong 1 cycle.
- Không drop/rename nóng.
- Checklist: tạo file migration, script chuyển dữ liệu (nếu cần), test up/down, cập nhật ERD/docs.
