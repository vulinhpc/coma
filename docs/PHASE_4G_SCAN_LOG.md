# PHASE 4G SCAN LOG — FORBIDDEN DB CALLS DETECTION

**Ngày scan:** 06/10/2025 17:15:00  
**Mục tiêu:** Phát hiện tất cả vi phạm `frappe.db` operations trong codebase COMA

---

## 🚨 KẾT QUẢ SCAN

**Tổng số vi phạm phát hiện:** 22 vi phạm trong 12 files

---

## 📋 CHI TIẾT VI PHẠM

### 1. **expense_calculator.py** (2 vi phạm)
```
apps/coma/coma/services/expense_calculator.py:75:        frappe.db.set_value('Project', doc.project, 'total_expense', result['net_expense'])
apps/coma/coma/services/expense_calculator.py:89:        frappe.db.set_value('Project', doc.project, 'total_expense', result['net_expense'])
```
**Mức độ:** 🔴 **NGHIÊM TRỌNG** - Cần thay thế ngay bằng `frappe.get_doc().save()`

### 2. **create_workspaces.py** (2 vi phạm)
```
apps/coma/coma/utils/create_workspaces.py:20:                if name and not frappe.db.exists("Workspace", name):
apps/coma/coma/utils/create_workspaces.py:32:    frappe.db.commit()
```
**Mức độ:** 🟡 **TRUNG BÌNH** - `exists()` có thể chấp nhận, `commit()` cần review

### 3. **seed_demo_data.py** (3 vi phạm)
```
apps/coma/coma/utils/seed_demo_data.py:12:            frappe.db.delete(doctype)
apps/coma/coma/utils/seed_demo_data.py:17:    frappe.db.commit()
apps/coma/coma/utils/seed_demo_data.py:100:    frappe.db.commit()
```
**Mức độ:** 🔴 **NGHIÊM TRỌNG** - `delete()` cần thay bằng `frappe.delete_doc()`

### 4. **sync_workspace_content.py** (2 vi phạm)
```
apps/coma/coma/utils/sync_workspace_content.py:31:                if name and frappe.db.exists("Workspace", name):
apps/coma/coma/utils/sync_workspace_content.py:55:    frappe.db.commit()
```
**Mức độ:** 🟡 **TRUNG BÌNH** - `exists()` có thể chấp nhận, `commit()` cần review

### 5. **create_dashboard_charts.py** (1 vi phạm)
```
apps/coma/coma/utils/create_dashboard_charts.py:103:    frappe.db.commit()
```
**Mức độ:** 🟡 **TRUNG BÌNH** - `commit()` cần review

### 6. **task.py** (1 vi phạm)
```
apps/coma/coma/coma/doctype/task/task.py:41:            frappe.db.commit()
```
**Mức độ:** 🟡 **TRUNG BÌNH** - `commit()` cần review

### 7. **project_expense_report.py** (1 vi phạm)
```
apps/coma/coma/coma/report/project_expense_report/project_expense_report.py:77:    data = frappe.db.sql(f"""
```
**Mức độ:** 🔴 **NGHIÊM TRỌNG** - Cần thay bằng QueryBuilder

### 8. **project_progress_report.py** (1 vi phạm)
```
apps/coma/coma/coma/report/project_progress_report/project_progress_report.py:95:    data = frappe.db.sql(f"""
```
**Mức độ:** 🔴 **NGHIÊM TRỌNG** - Cần thay bằng QueryBuilder

### 9. **auth.py** (2 vi phạm)
```
apps/coma/coma/api/v1/auth.py:66:    frappe.db.commit()
apps/coma/coma/api/v1/auth.py:86:    projects = frappe.db.sql("""
```
**Mức độ:** 🔴 **NGHIÊM TRỌNG** - `sql()` cần thay bằng QueryBuilder

### 10. **project.py** (2 vi phạm)
```
apps/coma/coma/api/v1/project.py:16:    projects = frappe.db.sql("""
apps/coma/coma/api/v1/project.py:300:    member = frappe.db.exists('Project Team Member', {
```
**Mức độ:** 🔴 **NGHIÊM TRỌNG** - `sql()` cần thay bằng QueryBuilder

### 11. **check_doctypes.py** (1 vi phạm)
```
apps/coma/coma/setup/check_doctypes.py:12:    result = frappe.db.sql("SELECT name FROM `tabDocType` WHERE module='COMA'")
```
**Mức độ:** 🔴 **NGHIÊM TRỌNG** - Cần thay bằng QueryBuilder

### 12. **auto_create_project_doctypes.py** (1 vi phạm)
```
apps/coma/coma/setup/auto_create_project_doctypes.py:725:			existing_count = frappe.db.count("Project", {
```
**Mức độ:** 🟡 **TRUNG BÌNH** - `count()` có thể chấp nhận

### 13. **reset_old_doctypes.py** (4 vi phạm)
```
apps/coma/coma/setup/reset_old_doctypes.py:26:            if frappe.db.exists("DocType", doctype_name):
apps/coma/coma/setup/reset_old_doctypes.py:28:                frappe.db.sql(f"DELETE FROM `tab{doctype_name}`")
apps/coma/coma/setup/reset_old_doctypes.py:36:                frappe.db.sql(f"DROP TABLE IF EXISTS `tab{doctype_name}`")
apps/coma/coma/setup/reset_old_doctypes.py:46:    frappe.db.commit()
```
**Mức độ:** 🔴 **NGHIÊM TRỌNG** - Setup script, cần review

---

## 📊 TỔNG KẾT PHÂN LOẠI

| Loại vi phạm | Số lượng | Mức độ | Ưu tiên |
|---------------|----------|---------|----------|
| `frappe.db.set_value()` | 2 | 🔴 NGHIÊM TRỌNG | 1 |
| `frappe.db.sql()` | 6 | 🔴 NGHIÊM TRỌNG | 1 |
| `frappe.db.delete()` | 1 | 🔴 NGHIÊM TRỌNG | 1 |
| `frappe.db.commit()` | 7 | 🟡 TRUNG BÌNH | 2 |
| `frappe.db.exists()` | 3 | 🟡 TRUNG BÌNH | 3 |
| `frappe.db.count()` | 1 | 🟡 TRUNG BÌNH | 3 |

---

## 🎯 KẾ HOẠCH REFACTOR

### **Ưu tiên 1 (NGAY LẬP TỨC):**
1. `expense_calculator.py` - Thay `set_value()` bằng `get_doc().save()`
2. `project_expense_report.py` - Thay `sql()` bằng QueryBuilder
3. `project_progress_report.py` - Thay `sql()` bằng QueryBuilder
4. `auth.py` - Thay `sql()` bằng QueryBuilder
5. `project.py` - Thay `sql()` bằng QueryBuilder
6. `check_doctypes.py` - Thay `sql()` bằng QueryBuilder
7. `seed_demo_data.py` - Thay `delete()` bằng `delete_doc()`

### **Ưu tiên 2 (SAU KHI HOÀN THÀNH ƯU TIÊN 1):**
8. Review và cleanup tất cả `frappe.db.commit()`
9. Review `frappe.db.exists()` usage
10. Review `frappe.db.count()` usage

### **Ưu tiên 3 (CUỐI CÙNG):**
11. Review setup scripts trong `setup/` folder

---

## 📝 GHI CHÚ

- **Tổng files cần refactor:** 12 files
- **Tổng vi phạm cần sửa:** 22 vi phạm
- **Thời gian ước tính:** 2-3 giờ
- **Rủi ro:** Thấp nếu tuân thủ đúng Frappe API patterns

---

**PHASE 4G SCAN COMPLETED – READY FOR REFACTOR**
