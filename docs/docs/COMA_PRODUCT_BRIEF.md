# COMA — Construction Management SaaS (Lean Product Brief)

## 🧩 Mục tiêu sản phẩm

Xây dựng nền tảng quản lý công trường **nhẹ, nhanh, rõ ràng**, phục vụ **doanh nghiệp xây dựng nhỏ–vừa**, giúp:

- Quản lý tiến độ, nhật ký, hình ảnh, chi phí, thành viên.
- Giảm thời gian xử lý báo cáo hàng ngày.
- Tăng tính minh bạch & trách nhiệm giữa các bên.

## 🎯 Giá trị cốt lõi

- **Nhanh**: thao tác như Zalo, load < 2s.
- **Dễ hiểu**: Shadcn Admin UI rõ ràng.
- **Thực địa**: upload ảnh/video từ di động.
- **Minh bạch**: nhật ký, chi phí, audit log.

## 👤 Đối tượng người dùng

- PM/Chỉ huy trưởng, Chủ đầu tư/Quản lý, Kế toán công trình, Admin công ty.

## ⚙️ Phạm vi MVP (v1)

1. Projects — CRUD + filter + member roles
2. Daily Logs — ghi nhật ký + Cloudinary upload
3. Transactions — chi phí/thu nhập
4. Reports — KPI cơ bản (ảnh, logs, thu/chi)
5. Auth & Roles — Clerk + RLS ứng dụng
6. Cloudinary — upload + preview + CDN

## 🚫 Không nằm trong v1

Offline, Mobile app riêng, Kế toán tích hợp, AI summarizer.

## 📅 KPI thành công

| Mục tiêu       | Thước đo | Mốc     |
| -------------- | -------- | ------- |
| Tạo nhật ký    | < 1 phút | Tuần 6  |
| Upload ổn định | > 98%    | Tuần 8  |
| Load dashboard | < 3s     | Tuần 10 |
| Team active    | ≥ 10     | MVP     |

## 🔧 Công nghệ

Next.js 14 + TS + Shadcn, Drizzle + Postgres, Clerk, Cloudinary, Vercel, Vitest + Playwright.
