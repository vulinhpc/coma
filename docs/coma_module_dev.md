# 🧱 Roadmap Phát Triển Module COMA (Frappe v15 Chuẩn)

## 📚 Tài Liệu Nền Tảng

**Tham khảo chính thức:**
- [Create an App](https://docs.frappe.io/framework/user/en/tutorial/create-an-app)
- [Create a DocType](https://docs.frappe.io/framework/user/en/tutorial/create-a-doctype)
- [Developer Mode](https://docs.frappe.io/framework/user/en/tutorial/create-a-doctype)
- [Modules & Desktop Config](https://docs.frappe.io/framework/user/en/basics/apps)
- [Migrating to v15](https://github.com/frappe/frappe/wiki/Migrating-to-version-15)

---

## 🛠 Giai Đoạn A — Khởi Tạo App & Cấu Hình Ban Đầu

| Bước | Hành động | Ghi chú |
|------|------------|-----------|
| A1 | Tạo app `coma` | `bench new-app coma` |
| A2 | Cài app vào site | `bench --site localhost install-app coma` |
| A3 | Bật developer mode | `bench set-config -g developer_mode true` |
| A4 | Build & restart | `bench build && bench restart` |
| A5 | Kiểm tra file `modules.txt` | Bảo đảm module hiển thị trong app |

✅ Kết quả: App COMA sẵn sàng, developer mode hoạt động.

---

## 🧩 Giai Đoạn B — Tạo Module / Desktop / Workspace

| Bước | Hành động | Ghi chú |
|------|------------|-----------|
| B1 | Tạo **Module Def** qua UI | Desk → Module Def → New → App = coma |
| B2 | Kiểm tra `modules.txt` | Module được thêm tự động |
| B3 | Tạo file `coma/config/desktop.py` |  
```python
from frappe import _

def get_data():
    return [
        {
            "module_name": "Construction Management",
            "color": "blue",
            "icon": "octicon octicon-tools",
            "type": "module",
            "label": _("Construction Management")
        }
    ]
``` |
| B4 | `bench build && bench restart` | Cập nhật Desk UI |
| B5 | (Tùy chọn) Tạo Workspace | Sử dụng Doctype Workspace |

✅ Module COMA xuất hiện trên Desk.

---

## 🧱 Giai Đoạn C — Tạo DocType

| Bước | Hành động | Lưu ý |
|------|------------|-----------|
| C1 | Bật developer mode | Bắt buộc cho scaffold DocType |
| C2 | Desk → DocType → New | Module = "Construction Management" |
| C3 | Lưu & Reload | Kiểm tra giao diện list/form |
| C4 | Export DocType | `bench export-fixtures` |
| C5 | Thêm file logic | `doctype_name.py`, `.js`, `.json` |
| C6 | `bench migrate` | Cập nhật DB |
| C7 | Kiểm tra permissions | Thiết lập role ngay từ đầu |

---

## ⚙️ Giai Đoạn D — Business Logic & Hooks

| Bước | Hành động | Ghi chú |
|------|------------|-----------|
| D1 | Định nghĩa hooks | Trong `hooks.py`: `doc_events`, `scheduler_events` |
| D2 | Viết function handler | validate, on_submit, after_insert... |
| D3 | Tách business logic | Trong `coma/services/...` |
| D4 | Dùng scheduler đúng chuẩn | `frappe.enqueue`, tránh job_name cũ |
| D5 | Kiểm tra mail / notify | `frappe.sendmail`, `frappe.publish_realtime` |

---

## 🌐 Giai Đoạn E — API Endpoint

| Bước | Hành động | Ghi chú |
|------|------------|-----------|
| E1 | Tạo file API | `coma/api/v1/*.py` |
| E2 | Đặt decorator `@frappe.whitelist()` | Cho mỗi method công khai |
| E3 | Kiểm tra permission | `frappe.has_permission`, `frappe.session.user` |
| E4 | Test qua Postman | Endpoint `/api/method/...` |

---

## 🪟 Giai Đoạn F — Portal / Web Pages

| Bước | Hành động | Ghi chú |
|------|------------|-----------|
| F1 | Folder `coma/www/...` | VD: `client_portal`, `engineer_mobile` |
| F2 | File `.py` + `.html` | Controller + Template |
| F3 | Dùng Jinja + API | Render context từ API |
| F4 | `bench build && bench clear-cache` | Xem kết quả trên web |

---

## 📊 Giai Đoạn G — Report & Dashboard

| Bước | Hành động | Ghi chú |
|------|------------|-----------|
| G1 | `bench make-report` | Sinh report trong app |
| G2 | Viết query / script report | Trong folder `coma/coma/report/...` |
| G3 | Tạo Dashboard | Doctype Dashboard / Chart |

---

## 👥 Giai Đoạn H — Role & Permission

| Bước | Hành động | Ghi chú |
|------|------------|-----------|
| H1 | Tạo Roles | COMA Owner, Engineer, Supervisor, Client |
| H2 | Role Permissions | Thiết lập trong DocType |
| H3 | Logic permission tuỳ chỉnh | `get_permission_query_conditions` |
| H4 | Tạo DocType Settings | Cho config module |

---

## 🧪 Giai Đoạn I — Kiểm Thử & i18n

| Bước | Hành động | Ghi chú |
|------|------------|-----------|
| I1 | Viết seed data | `coma/setup/seed.py` |
| I2 | Kiểm tra luồng nghiệp vụ | Create → Submit → Approve |
| I3 | Dịch ngôn ngữ | `coma/translations/vi.csv` |
| I4 | Export fixtures | Giữ cấu hình stable |

---

## 🚀 Giai Đoạn J — Đóng Gói & Deploy

| Bước | Hành động | Ghi chú |
|------|------------|-----------|
| J1 | Kiểm tra code style | flake8 / black / eslint |
| J2 | Export fixtures / patches | `bench export-fixtures` |
| J3 | Test migrate | `bench migrate` |
| J4 | Test staging | Deploy demo site |
| J5 | Đóng gói app | Commit & push GitHub |

---

## ✅ Checklist Cuối

- [ ] Developer mode = True  
- [ ] Module Def hiển thị trên Desk  
- [ ] Tất cả DocType thuộc module COMA  
- [ ] Hooks, workflow, scheduler chuẩn  
- [ ] API an toàn & test qua Postman  
- [ ] Roles & Permissions phù hợp  
- [ ] Seed data demo đầy đủ  
- [ ] Fixtures & patches sẵn sàng  
- [ ] i18n hoàn chỉnh  
- [ ] Test E2E trước deploy

