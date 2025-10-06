# 📋 COMA - Construction Management App

**Developer:** Vu Linh (mrlinhvu1987@gmail.com)  
**Framework:** Frappe  
**Version:** MVP Ultra Simple  
**Last Updated:** 2025-10-06

---

## 📖 MÔ TẢ DỰ ÁN

### Tổng quan
COMA là ứng dụng quản lý dự án xây dựng đơn giản, tập trung vào 2 chức năng cốt lõi:
1. **Theo dõi tiến độ** công việc hàng ngày
2. **Quản lý thu chi** dự án

### Đặc điểm
- **Đơn giản tối đa:** Bỏ tất cả tính năng phức tạp, chỉ giữ những gì thực sự cần
- **Mobile-first:** Tối ưu cho Engineer nhập liệu trên công trường
- **Tách bạch:** Tiến độ và Chi phí là 2 module độc lập, không ràng buộc
- **Tiếng Việt:** UI/UX ưu tiên tiếng Việt, code bằng tiếng Anh

### Phạm vi MVP
✅ **CÓ:**
- Quản lý dự án, hạng mục, đầu việc
- Nhật ký công việc hàng ngày (mô tả + ảnh)
- Cập nhật trạng thái công việc
- Tính tiến độ tự động (theo trọng số)
- Ghi nhận thu chi riêng biệt
- 2 báo cáo: Tiến độ & Chi phí

❌ **KHÔNG CÓ:**
- Khối lượng công việc chi tiết
- Đơn giá, đơn vị đo
- Quản lý nhà thầu
- Quản lý vật tư kho
- QC/QA checklist
- Change order
- Client portal
- Liên kết chi phí với công việc cụ thể

---

## 🏗️ KIẾN TRÚC HỆ THỐNG

### DocTypes (5 loại)

```
1. Project (Dự án)
   ├── team_members (child table)
   ├── Categories (1-n)
   └── Expense Entries (1-n)

2. Category (Hạng mục)
   ├── Tasks (1-n)
   └── CHỈ có: tên, trọng số, tiến độ%, trạng thái

3. Task (Đầu việc)
   ├── Daily Logs (1-n)
   └── CHỈ có: tên, trọng số, tiến độ%, trạng thái, người làm

4. Daily Log (Nhật ký)
   └── CHỈ có: mô tả công việc, ảnh, thời tiết, ghi chú

5. Expense Entry (Thu chi)
   └── CHỈ liên kết Project, KHÔNG liên kết Category/Task
```

### Luồng dữ liệu

**LUỒNG 1: TIẾN ĐỘ**
```
Task Status Changed
    ↓
Calculate Task Progress (0% / 50% / 100%)
    ↓
Calculate Category Progress (weighted average)
    ↓
Calculate Project Progress (weighted average)
```

**LUỒNG 2: CHI PHÍ**
```
Expense Entry Approved
    ↓
Sum all Expense Entries
    ↓
Update Project Total Expense
```

**HOÀN TOÀN TÁCH BIỆT!**

---

## 🗂️ CẤU TRÚC THƯ MỤC

```
coma/
├── coma/
│   ├── __init__.py
│   ├── config/
│   │   └── desktop.py              # Cấu hình workspace
│   ├── modules.txt                 # Danh sách modules
│   │
│   ├── coma/                       # Module chính
│   │   ├── doctype/
│   │   │   ├── project/           # Dự án
│   │   │   ├── category/          # Hạng mục
│   │   │   ├── task/              # Đầu việc
│   │   │   ├── daily_log/         # Nhật ký
│   │   │   └── expense_entry/     # Thu chi
│   │   │
│   │   └── report/
│   │       ├── project_progress_report/    # Báo cáo tiến độ
│   │       └── project_expense_report/     # Báo cáo chi phí
│   │
│   ├── api/
│   │   └── v1/
│   │       ├── __init__.py
│   │       ├── auth.py            # Login/Logout
│   │       └── project.py         # CRUD operations
│   │
│   ├── services/
│   │   └── progress_calculator.py # Tính tiến độ
│   │
│   ├── utils/
│   │   └── helpers.py             # Helper functions
│   │
│   └── public/
│       ├── css/
│       ├── js/
│       └── images/
│
├── requirements.txt
└── README.md
```

---

## 🚀 ROADMAP PHÁT TRIỂN

### PHASE 1: Foundation (Tuần 1-2)
**Mục tiêu:** Setup project + tạo DocTypes cơ bản

#### Week 1: Setup & Core DocTypes
- [ ] Init Frappe app `bench new-app coma`
- [ ] Setup git repository
- [ ] Tạo DocType: Project
  - [ ] Fields theo spec
  - [ ] Child table: team_members
  - [ ] Permissions: Owner full, Member read
- [ ] Tạo DocType: Category
  - [ ] Fields: name, weight, progress%, status
  - [ ] Validation: tổng weight = 100%
- [ ] Tạo DocType: Task
  - [ ] Fields: name, weight, progress%, status, assignee
  - [ ] Validation: tổng weight trong category = 100%

#### Week 2: Daily Log & Expense
- [ ] Tạo DocType: Daily Log
  - [ ] Fields: work_description, photos (child table), weather
  - [ ] Photo child table: image, caption
  - [ ] Workflow: Draft → Submitted → Approved
- [ ] Tạo DocType: Expense Entry
  - [ ] Fields: entry_type, category_type, amount, description
  - [ ] Workflow: Draft → Approved
- [ ] Setup permissions cho tất cả DocTypes
- [ ] Test CRUD operations thủ công

**Deliverable:** 5 DocTypes hoạt động, có thể tạo/sửa/xóa được

---

### PHASE 2: Business Logic (Tuần 3)
**Mục tiêu:** Implement tính toán tiến độ tự động

#### Week 3: Progress Calculation Engine
- [ ] Tạo file `services/progress_calculator.py`
- [ ] Implement function `calculate_task_progress(task)`
  - [ ] Map status → progress% (0/50/100)
- [ ] Implement function `calculate_category_progress(category)`
  - [ ] Weighted average từ tasks
  - [ ] Fallback: simple average nếu không có weight
- [ ] Implement function `calculate_project_progress(project)`
  - [ ] Weighted average từ categories
  - [ ] Fallback: simple average nếu không có weight
- [ ] Setup hooks trong `hooks.py`:
  ```python
  doc_events = {
      "Task": {
          "on_update": "coma.services.progress_calculator.on_task_update"
      }
  }
  ```
- [ ] Test auto-update:
  - [ ] Update task status → check task progress
  - [ ] Check category progress auto-update
  - [ ] Check project progress auto-update
- [ ] Implement `calculate_project_expense(project)`
  - [ ] Sum all approved expense entries
  - [ ] Update project.total_expense

**Deliverable:** Progress tự động tính khi update task status

---

### PHASE 3: API & Reports (Tuần 4)
**Mục tiêu:** REST API cho mobile + 2 báo cáo

#### Week 4.1: API Development
- [ ] `api/v1/auth.py`:
  - [ ] `login(email, password)` → return API key
  - [ ] `get_user_profile()` → user info + projects
- [ ] `api/v1/project.py`:
  - [ ] `get_my_projects()` → list projects
  - [ ] `get_project_details(project_id)` → full hierarchy
  - [ ] `submit_daily_log(data)` → create daily log
  - [ ] `update_task_status(task_id, status)` → update + recalc
  - [ ] `submit_expense(data)` → create expense entry
  - [ ] `get_project_summary(project_id)` → progress + expense
- [ ] Test all endpoints với Postman/Insomnia
- [ ] Write API documentation

#### Week 4.2: Reports
- [ ] Report: Project Progress Report
  - [ ] Columns: Project, Category, Task, Status, Progress%
  - [ ] Filters: Project, Date, Status
  - [ ] Summary: Overall progress, task count
- [ ] Report: Project Expense Report
  - [ ] Columns: Date, Type, Category, Amount, Description
  - [ ] Filters: Project, Date range, Entry type
  - [ ] Summary: Total budget, expense, remaining
- [ ] Test reports với sample data

**Deliverable:** API hoạt động + 2 báo cáo có dữ liệu

---

### PHASE 4: UI/UX & Testing (Tuần 5-6)
**Mục tiêu:** Polish UI + Beta testing

#### Week 5: UI/UX Polish
- [ ] Custom CSS cho form views
  - [ ] Project card view với cover image
  - [ ] Task kanban board (optional)
- [ ] Mobile responsive check
  - [ ] Daily Log form mobile-friendly
  - [ ] Photo upload optimization
- [ ] Dashboard cho Project
  - [ ] Progress chart (gauge/donut)
  - [ ] Expense summary
  - [ ] Recent logs list
- [ ] Vietnamese translations
  - [ ] Translate all labels
  - [ ] Date/number format VN
- [ ] User guide documentation
  - [ ] Hướng dẫn tạo dự án
  - [ ] Hướng dẫn nhập daily log
  - [ ] Hướng dẫn xem báo cáo

#### Week 6: Testing & Deploy
- [ ] Tạo sample data:
  - [ ] 3 projects với 5-10 categories mỗi project
  - [ ] 20-30 tasks per project
  - [ ] 50+ daily logs
  - [ ] 30+ expense entries
- [ ] Internal testing:
  - [ ] Test tất cả workflows
  - [ ] Test progress calculation với nhiều scenarios
  - [ ] Test permissions (Owner, PM, Member)
  - [ ] Test API với mobile app (nếu có)
- [ ] Beta testing với 2-3 dự án thật:
  - [ ] Onboard 2-3 khách hàng pilot
  - [ ] Training session
  - [ ] Collect feedback
  - [ ] Fix critical bugs
- [ ] Deploy production:
  - [ ] Setup production server
  - [ ] SSL certificate
  - [ ] Backup strategy
  - [ ] Monitoring setup

**Deliverable:** App sẵn sàng production với 2-3 khách hàng pilot

---

## 📊 DEFINITION OF DONE

### Phase 1 ✅
- [ ] Có thể tạo Project với team members
- [ ] Có thể tạo Categories với weight = 100%
- [ ] Có thể tạo Tasks với weight = 100%
- [ ] Có thể tạo Daily Log với photos
- [ ] Có thể tạo Expense Entry

### Phase 2 ✅
- [ ] Update task status → Task progress tự động update
- [ ] Task progress update → Category progress tự động update
- [ ] Category progress update → Project progress tự động update
- [ ] Approve expense → Project total_expense tự động update
- [ ] Không có lỗi calculation

### Phase 3 ✅
- [ ] API login trả về API key hợp lệ
- [ ] API get_my_projects trả về list projects
- [ ] API submit_daily_log tạo được log + upload ảnh
- [ ] API update_task_status trigger được progress recalc
- [ ] 2 Reports hiển thị đúng data

### Phase 4 ✅
- [ ] UI responsive trên mobile
- [ ] Forms dễ nhập liệu
- [ ] Reports dễ đọc
- [ ] 100% translated sang tiếng Việt
- [ ] 2-3 khách hàng pilot sử dụng được
- [ ] Không có critical bugs

---

## 🎯 SUCCESS METRICS

### Technical Metrics
- Response time API < 500ms
- Page load time < 2s
- Mobile photo upload < 5s
- Zero critical bugs in production
- 95% uptime

### User Metrics
- Engineer có thể nhập daily log < 3 phút
- PM có thể xem tiến độ dự án < 30 giây
- Owner có thể xem báo cáo chi phí < 1 phút

### Business Metrics
- 2-3 pilot customers onboarded
- 80% user satisfaction (survey)
- 50+ daily logs created per week
- Ready to scale to 10+ projects

---

## 🔧 TECH STACK

- **Backend:** Frappe Framework (Python)
- **Database:** MariaDB
- **Frontend:** Frappe UI (Jinja2 + Vue.js)
- **API:** REST (Frappe whitelist)
- **Deployment:** 
  - Development: `bench start`
  - Production: Nginx + Supervisor + Redis
- **Version Control:** Git + GitHub

---

## 📝 NOTES

### Nguyên tắc phát triển
1. **KISS:** Keep It Simple, Stupid
2. **YAGNI:** You Aren't Gonna Need It - không làm tính năng chưa cần
3. **MVP First:** Làm đủ để khách hàng dùng được, không phải làm hoàn hảo
4. **User-Centric:** Hỏi ý kiến user thường xuyên
5. **Iterative:** Release nhỏ, cải tiến dần

### Những gì CÓ THỂ thêm sau MVP
- Contractor management
- Material stock tracking
- QC checklist
- Change order
- Client portal
- Gantt chart
- Budget vs actual comparison per task
- Photo geolocation
- Offline mode
- Push notifications

### Những gì KHÔNG LÀM trong MVP
- Quantity tracking (khối lượng)
- Unit cost (đơn giá)
- Complex approval workflow
- Multi-currency
- Integration với accounting software
- AI/ML predictions
- Advanced analytics

---

## 📞 SUPPORT

**Developer:** Vu Linh  
**Email:** mrlinhvu1987@gmail.com  
**Documentation:** [Link to docs]  
**Issue Tracker:** [Link to GitHub issues]

---

**CHÚ Ý:** Document này là bản mô tả chi tiết nhất cho việc implement. Đọc kỹ từng section trước khi bắt đầu code. Mọi thay đổi spec phải update document này trước!