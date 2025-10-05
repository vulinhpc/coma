# 📋 MÔ TẢ DỰ ÁN MVP (Frappe App: **COMA** — Construction Management)

*Cập nhật: 2025-10-05*  
*Developer: Vu Linh | Email: mrlinhvu1987@gmail.com*

---

## 1) Định hướng chung

- **Tên app:** `coma` (Construction Management)
- **Ngôn ngữ:** đa ngôn ngữ, ưu tiên **tiếng Việt trước** (VN-first).
- **Code convention:** tất cả biến, hàm, file, thư mục trong code sử dụng **tiếng Anh** để dễ maintain.
- **Triển khai:** SaaS đa tenant (site-per-tenant hoặc org-per-tenant).
- **Giao diện:** tối giản, role-based, phân biệt rõ người dùng văn phòng (PM/Owner) và công trường (Engineer/Supervisor/QC).
- **Triết lý UX:** "điền nhanh – duyệt nhanh – xem nhanh", mobile-first cho công trường, dashboard rõ ràng cho PM/Owner.

---

## 2) Cấu trúc ứng dụng (dự kiến)

```
coma/
  ├── coma/
  │   ├── __init__.py
  │   ├── config/
  │   │   ├── desktop.py        # Workspace, module config
  │   │   ├── docs.py           # API docs config
  │   ├── modules.txt           # Danh sách module trong app
  │   ├── coma/
  │   │   ├── doctype/
  │   │   │   ├── project/
  │   │   │   ├── category/
  │   │   │   ├── task/
  │   │   │   ├── member/
  │   │   │   ├── contractor/
  │   │   │   ├── daily_progress_log/
  │   │   │   ├── daily_resource_log/
  │   │   │   ├── daily_log_photo/
  │   │   │   ├── change_order/
  │   │   │   ├── project_document/
  │   │   │   ├── material_stock_entry/
  │   │   │   ├── qc_checklist/
  │   │   │   └── qc_check_item/
  │   │   └── report/
  │   ├── api/                  # REST endpoints cho mobile app/portal
  │   │   ├── v1/
  │   │   │   ├── __init__.py
  │   │   │   ├── auth.py
  │   │   │   ├── engineer.py
  │   │   │   ├── supervisor.py
  │   │   │   ├── client.py
  │   ├── services/             # Business logic (workflow, calculation)
  │   │   ├── progress_calculator.py
  │   │   ├── cost_calculator.py
  │   │   ├── notification_service.py
  │   ├── utils/                # Helper functions
  │   │   ├── image_optimizer.py
  │   │   ├── validators.py
  │   │   ├── helpers.py
  │   ├── www/                  # Portal pages (Engineer portal, Share link)
  │   │   ├── client_portal/
  │   │   ├── engineer_mobile/
  │   └── public/
  │       ├── css/
  │       ├── js/
  │       └── images/
  ├── patches.txt               # Migration patches
  ├── requirements.txt          # Python dependencies
  └── README.md
```

---

## 3) DocType chi tiết

### 3.1 Project (Dự án)

- **Fields:**
  - `project_name` (Data, required)
  - `project_code` (Data, unique, auto-generated nếu để trống)
  - `client_name` (Data)
  - `client_phone` (Data, optional, toggle hiển thị ở share link)
  - `client_email` (Data, optional)
  - `address` (Small Text)
  - `location_map` (Data/URL, optional - Google Maps link)
  - `scale` (Data - VD: "300m2, 3 tầng")
  - `start_date` (Date, required)
  - `end_date` (Date, required)
  - `actual_start_date` (Date, auto-fill when status = In Progress)
  - `actual_end_date` (Date, auto-fill when status = Completed)
  - `status` (Select: Draft/In Progress/Paused/Completed/Cancelled)
  - `cover_image` (Attach Image, required)
  - `description` (Text Editor)
  - `total_budget` (Currency, optional)
  - `total_cost` (Currency, auto-calculated from Resource Logs)
  - `progress_percentage` (Percent, auto-calculated, read-only)
  - `client_portal_enabled` (Check, default=1)
  - `client_portal_url` (Data, auto-generated, read-only)

- **Child Tables:**
  - `members` (Table → Member)
  - `contractors` (Table → Contractor Assignment)

- **Permissions:**
  - Owner/PM: Full access
  - Engineer/Supervisor: Read project info, Write logs
  - QC: Read + Finalize logs
  - Client: Read-only via portal

### 3.2 Category (Hạng mục)

- **Fields:**
  - `project` (Link → Project, required)
  - `category_name` (Data, required)
  - `category_code` (Data, optional)
  - `planned_start` (Date)
  - `planned_end` (Date)
  - `actual_start` (Date, auto-fill)
  - `actual_end` (Date, auto-fill)
  - `progress_weight` (Float, optional, % trọng số trong tiến độ dự án, default=0)
  - `progress_percentage` (Percent, auto-calculated)
  - `status` (Select: Not Started/In Progress/Completed/Blocked)
  - `assigned_contractor` (Link → Contractor, optional)
  - `budget_amount` (Currency, optional)
  - `actual_cost` (Currency, auto-calculated)
  - `notes` (Small Text)

- **Validation:**
  - Tổng `progress_weight` của tất cả Categories trong 1 Project = 100%
  - `actual_start` phải >= Project start_date
  - `actual_end` phải <= Project end_date

### 3.3 Task (Đầu việc)

- **Fields:**
  - `project` (Link → Project, required)
  - `category` (Link → Category, required)
  - `task_name` (Data, required)
  - `task_code` (Data, optional)
  - `unit` (Select: m2/m3/tấn/bộ/m dài/cái/công, customizable)
  - `planned_quantity` (Float, optional)
  - `actual_quantity` (Float, auto-calculated from Daily Resource Logs)
  - `task_weight` (Float, % trọng số trong Category, default=0)
  - `progress_percentage` (Percent, auto-calculated = actual/planned * 100)
  - `assignee` (Link → User, optional)
  - `assigned_contractor` (Link → Contractor, optional)
  - `unit_cost` (Currency, optional - đơn giá)
  - `planned_cost` (Currency, calculated = planned_quantity * unit_cost)
  - `actual_cost` (Currency, calculated = actual_quantity * unit_cost)
  - `start_date` (Date, optional)
  - `end_date` (Date, optional)
  - `status` (Select: Not Started/In Progress/Completed/Blocked)
  - `notes` (Small Text)

- **Validation:**
  - Tổng `task_weight` trong 1 Category = 100%

### 3.4 Member (Thành viên dự án)

- **Fields:**
  - `project` (Link → Project, required)
  - `user` (Link → User, required)
  - `role` (Select: Owner/PM/Engineer/Supervisor/QC/Admin)
  - `active` (Check, default=1)
  - `joined_date` (Date, default=Today)
  - `left_date` (Date, optional)
  - `phone` (Data, optional)
  - `notes` (Small Text)

- **Validation:**
  - 1 Project phải có ít nhất 1 Owner hoặc PM
  - Không duplicate user trong cùng 1 project

### 3.5 Contractor (Nhà thầu phụ)

- **Fields:**
  - `contractor_name` (Data, required, unique)
  - `contractor_code` (Data, optional, unique)
  - `contractor_type` (Select: Labor/Material/Equipment/Subcontractor/Mixed)
  - `contact_person` (Data, required)
  - `phone` (Data, required)
  - `email` (Data, optional)
  - `address` (Small Text)
  - `tax_code` (Data, optional)
  - `bank_account` (Small Text, optional)
  - `contract_terms` (Text Editor, optional)
  - `payment_terms` (Select: Monthly/Milestone/Daily/Weekly/Upon Completion)
  - `status` (Select: Active/Inactive/Blacklisted)
  - `rating` (Rating, 1-5 stars)
  - `notes` (Small Text)

- **Child Tables:**
  - `project_assignments` (Table: Project + Contract Value + Start Date + End Date)

### 3.6 Daily Progress Log (Nhật ký tiến độ)

- **Mục đích:** báo cáo tiến độ, minh chứng cho khách hàng.
- **Fields:**
  - `project` (Link → Project, required)
  - `category` (Link → Category, required)
  - `tasks` (Table: Link → Task, multiple selection, required)
  - `date` (Date, default=Today, required)
  - `shift` (Select: Morning/Afternoon/Night/Full Day)
  - `weather` (Select: Sunny/Rainy/Cloudy/Stormy, optional)
  - `temperature` (Data, optional - VD: "28-32°C")
  - `description` (Text Editor, required, min 50 characters)
  - `work_completed` (Text Editor, optional - Công việc hoàn thành cụ thể)
  - `work_planned_next` (Small Text, optional - Kế hoạch ngày mai)
  - `issues_encountered` (Small Text, optional)
  - `photos` (Table → Daily Log Photo, required ≥1, max 10)
  - `created_by` (Link → User, auto-fill)
  - `reviewed_by` (Link → User, auto-fill when Supervisor reviews)
  - `qc_by` (Link → User, auto-fill when QC finalizes)
  - `status` (Workflow: Draft → Pending Supervisor → Approved → Finalized by QC → Rejected)
  - `supervisor_comment` (Small Text)
  - `qc_rating` (Select: Pass/Fail/Pass with Minor Issues/Pass with Major Issues)
  - `qc_comment` (Small Text)
  - `qc_checklist` (Table → QC Check Item, optional)
  - `client_visible` (Check, default=1, control visibility in portal)
  - `submitted_at` (Datetime, auto-fill)
  - `approved_at` (Datetime, auto-fill)
  - `finalized_at` (Datetime, auto-fill)

- **Chia sẻ:** Yes (Client Portal) nhưng **ẩn toàn bộ số liệu khối lượng/chi phí**.

- **Workflow Transitions:**
  1. Engineer: Draft → Submit → Pending Supervisor Review
  2. Supervisor: Approve → Approved / Decline → Draft (với comment)
  3. QC: Finalize (rating + comment) → Finalized
  4. Optional: Supervisor/QC có thể Reject → Draft

- **Notifications:**
  - Submit → notify Supervisor
  - Approved → notify QC + Engineer
  - Finalized → notify Client (email) + Engineer
  - Rejected → notify Engineer với lý do

### 3.7 Daily Resource Log (Nhật ký nguồn lực nội bộ)

- **Mục đích:** quản lý nhân công, vật tư, máy móc, khối lượng để hạch toán nội bộ.
- **Fields:**
  - `project` (Link → Project, required)
  - `category` (Link → Category, required)
  - `task` (Link → Task, required)
  - `date` (Date, default=Today, required)
  - `shift` (Select: Morning/Afternoon/Night/Full Day)
  
  **Labor Section:**
  - `labor_count` (Int, default=0)
  - `labor_type` (Select: Skilled/Unskilled/Supervisor/Foreman)
  - `labor_cost_per_day` (Currency, optional)
  - `total_labor_cost` (Currency, calculated = labor_count * labor_cost_per_day)
  - `contractor` (Link → Contractor, optional)
  
  **Material Section:**
  - `materials` (Table: material_type [Link → Item], quantity, unit, unit_cost, total_cost)
  
  **Equipment/Machine Section:**
  - `equipment` (Table: machine_type [Link → Equipment], hours_used, hourly_rate, total_cost)
  
  **Progress Section:**
  - `actual_quantity` (Float, required - khối lượng hoàn thành trong ngày)
  - `unit` (Data, auto-fill from Task)
  
  **Issues & Notes:**
  - `issues` (Table: issue_type [Select], severity [Select: Low/Medium/High/Critical], description, resolution_status)
  - `weather` (Select: Sunny/Rainy/Cloudy/Stormy)
  - `weather_impact` (Select: None/Minor Delay/Major Delay/Work Stopped)
  - `notes` (Small Text)
  
  **Workflow:**
  - `created_by` (Link → User, auto-fill)
  - `reviewed_by` (Link → User, auto-fill when Supervisor reviews)
  - `status` (Workflow: Draft → Submitted → Approved → Rejected)
  - `submitted_at` (Datetime)
  - `approved_at` (Datetime)

- **Chia sẻ:** No (nội bộ).
- **Liên kết Finance:** dùng dữ liệu này × đơn giá để tính chi phí.
- **Auto-update:** Khi approved, tự động cộng `actual_quantity` vào Task.actual_quantity

### 3.8 Daily Log Photo (Ảnh nhật ký)

- **Fields:**
  - `parent` (Link → Daily Progress Log)
  - `parentfield` (Data = "photos")
  - `parenttype` (Data = "Daily Progress Log")
  - `image` (Attach Image, required)
  - `caption` (Small Text, max 200 characters)
  - `taken_at` (Datetime, optional - thời gian chụp)
  - `location` (Geolocation, optional - GPS coordinates nếu có)
  - `featured` (Check, default=0 - đánh dấu ảnh nổi bật cho portal)

- **Validation:**
  - Max file size: 10MB
  - Allowed types: .jpg, .jpeg, .png
  - Auto-optimize: resize to max 1920x1080, compress to 80% quality

### 3.9 Change Order (Lệnh thay đổi)

- **Mục đích:** quản lý thay đổi phạm vi, thiết kế, vật liệu do client yêu cầu hoặc phát sinh.
- **Fields:**
  - `project` (Link → Project, required)
  - `change_order_number` (Data, auto-generated, unique)
  - `category` (Link → Category, optional)
  - `change_type` (Select: Scope Change/Material Change/Design Change/Addition/Reduction/Other)
  - `title` (Data, required)
  - `description` (Text Editor, required)
  - `reason` (Select: Client Request/Site Condition/Design Error/Material Unavailable/Regulation Change/Other)
  - `requested_by` (Link → User, required)
  - `requested_date` (Date, default=Today)
  
  **Impact Assessment:**
  - `cost_impact` (Currency, required - có thể âm nếu giảm chi phí)
  - `time_impact_days` (Int, required - số ngày ảnh hưởng đến tiến độ)
  - `affected_tasks` (Table: Link → Task)
  - `new_end_date` (Date, calculated from time_impact)
  
  **Approval:**
  - `status` (Workflow: Draft → Submitted → Under Review → Approved → Rejected → Completed)
  - `reviewed_by` (Link → User - PM/Owner)
  - `approved_by` (Link → User - Owner)
  - `client_approved` (Check, default=0)
  - `client_signature` (Signature, optional)
  - `approval_date` (Date)
  - `rejection_reason` (Small Text)
  
  **Documentation:**
  - `attachments` (Table: file, description)
  - `before_photos` (Table → Photo)
  - `after_photos` (Table → Photo, optional)
  
  **Execution:**
  - `executed_date` (Date, optional)
  - `actual_cost` (Currency, optional)
  - `actual_time_impact` (Int, optional)
  - `completion_notes` (Small Text)

- **Workflow:**
  1. Engineer/PM creates Draft
  2. Submit → Under Review by PM
  3. PM Review → send to Owner for Approval
  4. Owner Approve → Client notified for signature
  5. Client Approved → status = Approved, ready for execution
  6. After completed → status = Completed

### 3.10 Project Document (Tài liệu dự án)

- **Mục đích:** lưu trữ bản vẽ, hợp đồng, giấy phép, biên bản.
- **Fields:**
  - `project` (Link → Project, required)
  - `document_name` (Data, required)
  - `document_type` (Select: Drawing/Contract/Permit/Report/Invoice/Receipt/Certificate/Other)
  - `document_category` (Select: Design/Legal/Financial/Technical/Quality/Safety/Other)
  - `file` (Attach, required)
  - `version` (Data, default="1.0")
  - `version_notes` (Small Text, optional)
  - `uploaded_by` (Link → User, auto-fill)
  - `upload_date` (Datetime, auto-fill)
  - `effective_date` (Date, optional - ngày hiệu lực)
  - `expiry_date` (Date, optional - ngày hết hạn)
  - `status` (Select: Draft/Active/Superseded/Expired/Archived)
  - `related_category` (Link → Category, optional)
  - `related_change_order` (Link → Change Order, optional)
  - `tags` (Small Text, comma-separated)
  - `description` (Small Text)
  - `client_visible` (Check, default=0 - có hiển thị ở client portal không)
  - `superseded_by` (Link → Project Document, optional - tài liệu thay thế)

- **Features:**
  - Version control: khi upload file mới với cùng tên, tự động tăng version
  - Audit trail: track tất cả thay đổi
  - Search: full-text search trong document_name, tags, description

### 3.11 Material Stock Entry (Nhập xuất vật tư)

- **Mục đích:** theo dõi vật tư nhập/xuất kho công trường.
- **Fields:**
  - `project` (Link → Project, required)
  - `entry_type` (Select: Purchase/Transfer In/Consumption/Transfer Out/Return/Adjustment)
  - `entry_number` (Data, auto-generated, unique)
  - `date` (Date, default=Today, required)
  - `materials` (Table: material [Link → Item], quantity, unit, unit_cost, total_cost, batch_no, expiry_date)
  - `supplier` (Link → Supplier/Contractor, optional)
  - `warehouse` (Data, default="Main Site")
  - `category` (Link → Category, optional - xuất cho hạng mục nào)
  - `task` (Link → Task, optional - xuất cho task nào)
  - `reference_document` (Data, optional - số PO, hóa đơn)
  - `total_value` (Currency, auto-calculated)
  - `created_by` (Link → User, auto-fill)
  - `approved_by` (Link → User, optional)
  - `status` (Select: Draft/Submitted/Approved/Rejected)
  - `notes` (Small Text)

- **Stock Balance:**
  - Mỗi Material có virtual stock balance tính theo Project
  - Current Stock = Opening + Purchase + Transfer In - Consumption - Transfer Out

### 3.12 QC Checklist Template (Mẫu kiểm tra chất lượng)

- **Mục đích:** tạo template checklist cho từng loại công việc.
- **Fields:**
  - `template_name` (Data, required, unique)
  - `category` (Link → Category, optional)
  - `task_type` (Data, optional - loại công việc áp dụng)
  - `description` (Small Text)
  - `check_items` (Table: item_name, criteria, pass_criteria, check_type [Visual/Measurement/Test])
  - `active` (Check, default=1)

### 3.13 QC Check Item (Item kiểm tra trong Progress Log)

- **Fields:**
  - `parent` (Link → Daily Progress Log)
  - `check_item` (Data, required - tên tiêu chí kiểm tra)
  - `criteria` (Small Text - mô tả tiêu chuẩn)
  - `result` (Select: Pass/Fail/N/A)
  - `measured_value` (Data, optional - giá trị đo được)
  - `notes` (Small Text)
  - `photo` (Attach Image, optional - ảnh minh chứng)

---

## 4) Progress Calculation Engine

### 4.1 Công thức tính tiến độ

```python
# services/progress_calculator.py

def calculate_task_progress(task):
    """
    Task Progress = (actual_quantity / planned_quantity) * 100
    Nếu planned_quantity = 0, dùng status-based:
      - Not Started: 0%
      - In Progress: 50%
      - Completed: 100%
    """
    if task.planned_quantity and task.planned_quantity > 0:
        return min((task.actual_quantity / task.planned_quantity) * 100, 100)
    else:
        status_map = {
            'Not Started': 0,
            'In Progress': 50,
            'Completed': 100,
            'Blocked': 0
        }
        return status_map.get(task.status, 0)

def calculate_category_progress(category):
    """
    Category Progress = Σ(Task Progress * Task Weight) / Σ(Task Weight)
    Nếu không có task weight, chia đều: Average(Task Progress)
    """
    tasks = frappe.get_all('Task', 
                           filters={'category': category.name},
                           fields=['name', 'task_weight'])
    
    if not tasks:
        return 0
    
    total_weight = sum(t.task_weight for t in tasks)
    
    if total_weight == 0:
        # Chia đều
        progress_sum = sum(calculate_task_progress(t) for t in tasks)
        return progress_sum / len(tasks)
    else:
        weighted_sum = sum(
            calculate_task_progress(t) * t.task_weight 
            for t in tasks
        )
        return weighted_sum / total_weight

def calculate_project_progress(project):
    """
    Project Progress = Σ(Category Progress * Category Weight) / Σ(Category Weight)
    Nếu không có category weight, chia đều
    """
    categories = frappe.get_all('Category',
                                filters={'project': project.name},
                                fields=['name', 'progress_weight'])
    
    if not categories:
        return 0
    
    total_weight = sum(c.progress_weight for c in categories)
    
    if total_weight == 0:
        progress_sum = sum(calculate_category_progress(c) for c in categories)
        return progress_sum / len(categories)
    else:
        weighted_sum = sum(
            calculate_category_progress(c) * c.progress_weight
            for c in categories
        )
        return weighted_sum / total_weight
```

### 4.2 Auto-update Triggers

```python
# Trong doctype hooks.py
doc_events = {
    "Daily Resource Log": {
        "on_submit": "coma.services.progress_calculator.update_task_progress",
        "on_cancel": "coma.services.progress_calculator.recalculate_task_progress"
    },
    "Task": {
        "on_update": "coma.services.progress_calculator.update_category_progress"
    },
    "Category": {
        "on_update": "coma.services.progress_calculator.update_project_progress"
    }
}
```

---

## 5) Cost Calculation Engine

### 5.1 Công thức tính chi phí

```python
# services/cost_calculator.py

def calculate_task_cost(task):
    """
    Planned Cost = planned_quantity * unit_cost
    Actual Cost = actual_quantity * unit_cost
                + Σ(labor_cost from Resource Logs)
                + Σ(material_cost from Resource Logs)
                + Σ(equipment_cost from Resource Logs)
    """
    planned = (task.planned_quantity or 0) * (task.unit_cost or 0)
    
    # Tổng từ Resource Logs
    resource_logs = frappe.get_all('Daily Resource Log',
                                   filters={'task': task.name, 'status': 'Approved'},
                                   fields=['total_labor_cost'])
    
    actual = sum(log.total_labor_cost or 0 for log in resource_logs)
    # + material cost + equipment cost (tương tự)
    
    return {
        'planned_cost': planned,
        'actual_cost': actual,
        'variance': actual - planned,
        'variance_percentage': ((actual - planned) / planned * 100) if planned else 0
    }

def calculate_category_cost(category):
    """
    Category Cost = Σ(Task Costs)
    """
    tasks = frappe.get_all('Task', filters={'category': category.name})
    
    planned_total = 0
    actual_total = 0
    
    for task in tasks:
        costs = calculate_task_cost(task)
        planned_total += costs['planned_cost']
        actual_total += costs['actual_cost']
    
    return {
        'budget_amount': category.budget_amount or planned_total,
        'actual_cost': actual_total,
        'variance': actual_total - (category.budget_amount or planned_total)
    }

def calculate_project_cost(project):
    """
    Project Cost = Σ(Category Costs) + Σ(Change Order Costs)
    """
    categories = frappe.get_all('Category', filters={'project': project.name})
    
    total_budget = project.total_budget or 0
    total_actual = 0
    
    for cat in categories:
        costs = calculate_category_cost(cat)
        total_actual += costs['actual_cost']
    
    # Thêm Change Orders
    change_orders = frappe.get_all('Change Order',
                                   filters={'project': project.name, 'status': 'Approved'},
                                   fields=['cost_impact'])
    change_order_cost = sum(co.cost_impact for co in change_orders)
    
    return {
        'total_budget': total_budget,
        'total_cost': total_actual,
        'change_order_cost': change_order_cost,
        'adjusted_budget': total_budget + change_order_cost,
        'variance': total_actual - (total_budget + change_order_cost),
        'budget_utilization': (total_actual / total_budget * 100) if total_budget else 0
    }
```

---

## 6) API Endpoints

### 6.1 Authentication

```python
# api/v1/auth.py

@frappe.whitelist(allow_guest=True)
def login(email, password):
    """
    Mobile app login
    Returns: api_key, api_secret, user_info
    """

@frappe.whitelist()
def logout():
    """
    Revoke API keys
    """

@frappe.whitelist()
def get_user_profile():
    """
    Get current user's profile + assigned projects
    """
```

### 6.2 Engineer Endpoints

```python
# api/v1/engineer.py

@frappe.whitelist()
def get_my_projects():
    """
    List projects where current user is a member
    Returns: project_list with basic info
    """

@frappe.whitelist()
def get_project_details(project_id):
    """
    Get full project info + categories + tasks
    """

@frappe.whitelist()
def get_tasks_by_category(category_id):
    """
    Get all tasks in a category for dropdown
    """

@frappe.whitelist()
def submit_progress_log(data):
    """
    Submit Daily Progress Log with photos
    Input: {
        project, category, tasks[], date, shift,
        description, photos[]
    }
    Returns: log_id, status
    """

@frappe.whitelist()
def submit_resource_log(data):
    """
    Submit Daily Resource Log
    Input: {
        project, category, task, date,
        labor_count, materials[], equipment[],
        actual_quantity
    }
    """

@frappe.whitelist()
def upload_photo(log_id, photo_file, caption):
    """
    Upload photo to existing log
    Uses Frappe file upload
    """

@frappe.whitelist()
def get_my_logs(filters):
    """
    Get logs created by current user
    Filters: date_range, project, status
    """
```

### 6.3 Supervisor Endpoints

```python
# api/