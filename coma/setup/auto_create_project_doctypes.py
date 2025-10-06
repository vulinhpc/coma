#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
COMA App - Auto Create Project DocTypes
Tự động tạo 3 DocTypes: Project Member, Project Contractor Assignment, Project
"""

import os
import json
from datetime import datetime

def create_project_member_doctype():
    """Tạo DocType Project Member (Child Table)"""
    print("1️⃣  Tạo Project Member...")
    
    # Tạo thư mục
    doctype_path = "/home/lroot/frappe-bench/apps/coma/coma/coma/doctype/project_member"
    os.makedirs(doctype_path, exist_ok=True)
    
    # Tạo __init__.py
    with open(f"{doctype_path}/__init__.py", "w") as f:
        f.write("")
    
    # Tạo JSON file
    project_member_json = {
        "actions": [],
        "allow_rename": 1,
        "autoname": "field:member_name",
        "creation": datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"),
        "default_view": "List",
        "doctype": "DocType",
        "editable_grid": 1,
        "engine": "InnoDB",
        "field_order": [
            "member_name",
            "column_break_2",
            "role",
            "section_break_4",
            "employee",
            "column_break_6",
            "contractor",
            "section_break_8",
            "start_date",
            "column_break_10",
            "end_date",
            "section_break_12",
            "hourly_rate",
            "column_break_14",
            "is_active"
        ],
        "fields": [
            {
                "fieldname": "member_name",
                "fieldtype": "Data",
                "in_list_view": 1,
                "label": "Member Name",
                "reqd": 1
            },
            {
                "fieldname": "column_break_2",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "role",
                "fieldtype": "Select",
                "in_list_view": 1,
                "label": "Role",
                "options": "Project Manager\nSite Engineer\nForeman\nWorker\nContractor",
                "reqd": 1
            },
            {
                "fieldname": "section_break_4",
                "fieldtype": "Section Break",
                "label": "Assignment"
            },
            {
                "fieldname": "employee",
                "fieldtype": "Link",
                "label": "Employee",
                "options": "Employee"
            },
            {
                "fieldname": "column_break_6",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "contractor",
                "fieldtype": "Link",
                "label": "Contractor",
                "options": "Supplier"
            },
            {
                "fieldname": "section_break_8",
                "fieldtype": "Section Break",
                "label": "Duration"
            },
            {
                "fieldname": "start_date",
                "fieldtype": "Date",
                "label": "Start Date",
                "reqd": 1
            },
            {
                "fieldname": "column_break_10",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "end_date",
                "fieldtype": "Date",
                "label": "End Date"
            },
            {
                "fieldname": "section_break_12",
                "fieldtype": "Section Break",
                "label": "Compensation"
            },
            {
                "fieldname": "hourly_rate",
                "fieldtype": "Currency",
                "label": "Hourly Rate"
            },
            {
                "fieldname": "column_break_14",
                "fieldtype": "Column Break"
            },
            {
                "default": "1",
                "fieldname": "is_active",
                "fieldtype": "Check",
                "label": "Is Active"
            }
        ],
        "istable": 1,
        "links": [],
        "modified": datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"),
        "modified_by": "Administrator",
        "module": "COMA",
        "name": "Project Member",
        "naming_rule": "By fieldname",
        "owner": "Administrator",
        "permissions": [
            {
                "create": 1,
                "delete": 1,
                "email": 1,
                "export": 1,
                "print": 1,
                "read": 1,
                "report": 1,
                "role": "System Manager",
                "share": 1,
                "write": 1
            }
        ],
        "sort_field": "modified",
        "sort_order": "DESC",
        "states": []
    }
    
    with open(f"{doctype_path}/project_member.json", "w", encoding="utf-8") as f:
        json.dump(project_member_json, f, indent=2, ensure_ascii=False)
    
    # Tạo Python file
    project_member_py = '''# -*- coding: utf-8 -*-
# Copyright (c) 2024, COMA and contributors
# For license information, please see license.txt

from frappe.model.document import Document

class ProjectMember(Document):
	pass
'''
    
    with open(f"{doctype_path}/project_member.py", "w", encoding="utf-8") as f:
        f.write(project_member_py)
    
    print(f"✅ Đã tạo: {doctype_path}/project_member.json")
    print(f"✅ Đã tạo: {doctype_path}/project_member.py")

def create_project_contractor_assignment_doctype():
    """Tạo DocType Project Contractor Assignment (Child Table)"""
    print("2️⃣  Tạo Project Contractor Assignment...")
    
    # Tạo thư mục
    doctype_path = "/home/lroot/frappe-bench/apps/coma/coma/coma/doctype/project_contractor_assignment"
    os.makedirs(doctype_path, exist_ok=True)
    
    # Tạo __init__.py
    with open(f"{doctype_path}/__init__.py", "w") as f:
        f.write("")
    
    # Tạo JSON file
    project_contractor_assignment_json = {
        "actions": [],
        "allow_rename": 1,
        "autoname": "field:contractor_name",
        "creation": datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"),
        "default_view": "List",
        "doctype": "DocType",
        "editable_grid": 1,
        "engine": "InnoDB",
        "field_order": [
            "contractor_name",
            "column_break_2",
            "contractor_type",
            "section_break_4",
            "contractor",
            "column_break_6",
            "contact_person",
            "section_break_8",
            "work_description",
            "section_break_10",
            "contract_value",
            "column_break_12",
            "currency",
            "section_break_14",
            "start_date",
            "column_break_16",
            "end_date",
            "section_break_18",
            "status",
            "column_break_20",
            "completion_percentage"
        ],
        "fields": [
            {
                "fieldname": "contractor_name",
                "fieldtype": "Data",
                "in_list_view": 1,
                "label": "Contractor Name",
                "reqd": 1
            },
            {
                "fieldname": "column_break_2",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "contractor_type",
                "fieldtype": "Select",
                "in_list_view": 1,
                "label": "Contractor Type",
                "options": "Civil Work\nElectrical\nPlumbing\nPainting\nLandscaping\nOther",
                "reqd": 1
            },
            {
                "fieldname": "section_break_4",
                "fieldtype": "Section Break",
                "label": "Contractor Details"
            },
            {
                "fieldname": "contractor",
                "fieldtype": "Link",
                "label": "Contractor",
                "options": "Supplier",
                "reqd": 1
            },
            {
                "fieldname": "column_break_6",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "contact_person",
                "fieldtype": "Data",
                "label": "Contact Person"
            },
            {
                "fieldname": "section_break_8",
                "fieldtype": "Section Break",
                "label": "Work Details"
            },
            {
                "fieldname": "work_description",
                "fieldtype": "Text",
                "label": "Work Description",
                "reqd": 1
            },
            {
                "fieldname": "section_break_10",
                "fieldtype": "Section Break",
                "label": "Contract Value"
            },
            {
                "fieldname": "contract_value",
                "fieldtype": "Currency",
                "label": "Contract Value",
                "reqd": 1
            },
            {
                "fieldname": "column_break_12",
                "fieldtype": "Column Break"
            },
            {
                "default": "USD",
                "fieldname": "currency",
                "fieldtype": "Link",
                "label": "Currency",
                "options": "Currency"
            },
            {
                "fieldname": "section_break_14",
                "fieldtype": "Section Break",
                "label": "Timeline"
            },
            {
                "fieldname": "start_date",
                "fieldtype": "Date",
                "label": "Start Date",
                "reqd": 1
            },
            {
                "fieldname": "column_break_16",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "end_date",
                "fieldtype": "Date",
                "label": "End Date",
                "reqd": 1
            },
            {
                "fieldname": "section_break_18",
                "fieldtype": "Section Break",
                "label": "Status"
            },
            {
                "default": "Not Started",
                "fieldname": "status",
                "fieldtype": "Select",
                "in_list_view": 1,
                "label": "Status",
                "options": "Not Started\nIn Progress\nCompleted\nOn Hold\nCancelled"
            },
            {
                "fieldname": "column_break_20",
                "fieldtype": "Column Break"
            },
            {
                "default": "0",
                "fieldname": "completion_percentage",
                "fieldtype": "Percent",
                "label": "Completion %"
            }
        ],
        "istable": 1,
        "links": [],
        "modified": datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"),
        "modified_by": "Administrator",
        "module": "COMA",
        "name": "Project Contractor Assignment",
        "naming_rule": "By fieldname",
        "owner": "Administrator",
        "permissions": [
            {
                "create": 1,
                "delete": 1,
                "email": 1,
                "export": 1,
                "print": 1,
                "read": 1,
                "report": 1,
                "role": "System Manager",
                "share": 1,
                "write": 1
            }
        ],
        "sort_field": "modified",
        "sort_order": "DESC",
        "states": []
    }
    
    with open(f"{doctype_path}/project_contractor_assignment.json", "w", encoding="utf-8") as f:
        json.dump(project_contractor_assignment_json, f, indent=2, ensure_ascii=False)
    
    # Tạo Python file
    project_contractor_assignment_py = '''# -*- coding: utf-8 -*-
# Copyright (c) 2024, COMA and contributors
# For license information, please see license.txt

from frappe.model.document import Document

class ProjectContractorAssignment(Document):
	pass
'''
    
    with open(f"{doctype_path}/project_contractor_assignment.py", "w", encoding="utf-8") as f:
        f.write(project_contractor_assignment_py)
    
    print(f"✅ Đã tạo: {doctype_path}/project_contractor_assignment.json")
    print(f"✅ Đã tạo: {doctype_path}/project_contractor_assignment.py")

def create_project_doctype():
    """Tạo DocType Project (Master DocType)"""
    print("3️⃣  Tạo Project...")
    
    # Tạo thư mục
    doctype_path = "/home/lroot/frappe-bench/apps/coma/coma/coma/doctype/project"
    os.makedirs(doctype_path, exist_ok=True)
    
    # Tạo __init__.py
    with open(f"{doctype_path}/__init__.py", "w") as f:
        f.write("")
    
    # Tạo JSON file
    project_json = {
        "actions": [],
        "allow_rename": 1,
        "autoname": "naming_series:",
        "creation": datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"),
        "default_view": "List",
        "doctype": "DocType",
        "editable_grid": 1,
        "engine": "InnoDB",
        "field_order": [
            "project_code",
            "column_break_2",
            "project_name",
            "section_break_4",
            "project_type",
            "column_break_6",
            "priority",
            "section_break_8",
            "project_description",
            "section_break_10",
            "client",
            "column_break_12",
            "project_manager",
            "section_break_14",
            "start_date",
            "column_break_16",
            "end_date",
            "section_break_18",
            "budget",
            "column_break_20",
            "currency",
            "section_break_22",
            "project_members",
            "section_break_24",
            "contractor_assignments",
            "section_break_26",
            "status",
            "column_break_28",
            "completion_percentage",
            "section_break_30",
            "notes"
        ],
        "fields": [
            {
                "fieldname": "project_code",
                "fieldtype": "Data",
                "in_list_view": 1,
                "label": "Project Code",
                "read_only": 1,
                "reqd": 1
            },
            {
                "fieldname": "column_break_2",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "project_name",
                "fieldtype": "Data",
                "in_list_view": 1,
                "label": "Project Name",
                "reqd": 1
            },
            {
                "fieldname": "section_break_4",
                "fieldtype": "Section Break",
                "label": "Basic Information"
            },
            {
                "fieldname": "project_type",
                "fieldtype": "Select",
                "in_list_view": 1,
                "label": "Project Type",
                "options": "Residential\nCommercial\nIndustrial\nInfrastructure\nRenovation\nOther",
                "reqd": 1
            },
            {
                "fieldname": "column_break_6",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "priority",
                "fieldtype": "Select",
                "label": "Priority",
                "options": "Low\nMedium\nHigh\nCritical",
                "reqd": 1
            },
            {
                "fieldname": "section_break_8",
                "fieldtype": "Section Break",
                "label": "Description"
            },
            {
                "fieldname": "project_description",
                "fieldtype": "Text",
                "label": "Project Description"
            },
            {
                "fieldname": "section_break_10",
                "fieldtype": "Section Break",
                "label": "Stakeholders"
            },
            {
                "fieldname": "client",
                "fieldtype": "Link",
                "label": "Client",
                "options": "Customer"
            },
            {
                "fieldname": "column_break_12",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "project_manager",
                "fieldtype": "Link",
                "label": "Project Manager",
                "options": "Employee"
            },
            {
                "fieldname": "section_break_14",
                "fieldtype": "Section Break",
                "label": "Timeline"
            },
            {
                "fieldname": "start_date",
                "fieldtype": "Date",
                "in_list_view": 1,
                "label": "Start Date",
                "reqd": 1
            },
            {
                "fieldname": "column_break_16",
                "fieldtype": "Column Break"
            },
            {
                "fieldname": "end_date",
                "fieldtype": "Date",
                "in_list_view": 1,
                "label": "End Date",
                "reqd": 1
            },
            {
                "fieldname": "section_break_18",
                "fieldtype": "Section Break",
                "label": "Budget"
            },
            {
                "fieldname": "budget",
                "fieldtype": "Currency",
                "label": "Budget",
                "reqd": 1
            },
            {
                "fieldname": "column_break_20",
                "fieldtype": "Column Break"
            },
            {
                "default": "USD",
                "fieldname": "currency",
                "fieldtype": "Link",
                "label": "Currency",
                "options": "Currency"
            },
            {
                "fieldname": "section_break_22",
                "fieldtype": "Section Break",
                "label": "Project Members"
            },
            {
                "fieldname": "project_members",
                "fieldtype": "Table",
                "label": "Project Members",
                "options": "Project Member",
                "reqd": 1
            },
            {
                "fieldname": "section_break_24",
                "fieldtype": "Section Break",
                "label": "Contractor Assignments"
            },
            {
                "fieldname": "contractor_assignments",
                "fieldtype": "Table",
                "label": "Contractor Assignments",
                "options": "Project Contractor Assignment"
            },
            {
                "fieldname": "section_break_26",
                "fieldtype": "Section Break",
                "label": "Status"
            },
            {
                "default": "Planning",
                "fieldname": "status",
                "fieldtype": "Select",
                "in_list_view": 1,
                "label": "Status",
                "options": "Planning\nIn Progress\nOn Hold\nCompleted\nCancelled"
            },
            {
                "fieldname": "column_break_28",
                "fieldtype": "Column Break"
            },
            {
                "default": "0",
                "fieldname": "completion_percentage",
                "fieldtype": "Percent",
                "label": "Completion %"
            },
            {
                "fieldname": "section_break_30",
                "fieldtype": "Section Break",
                "label": "Additional Information"
            },
            {
                "fieldname": "notes",
                "fieldtype": "Text",
                "label": "Notes"
            }
        ],
        "is_submittable": 1,
        "links": [],
        "modified": datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"),
        "modified_by": "Administrator",
        "module": "COMA",
        "name": "Project",
        "naming_rule": "By \"Naming Series\" field",
        "owner": "Administrator",
        "permissions": [
            {
                "create": 1,
                "delete": 1,
                "email": 1,
                "export": 1,
                "print": 1,
                "read": 1,
                "report": 1,
                "role": "System Manager",
                "share": 1,
                "submit": 1,
                "write": 1
            }
        ],
        "sort_field": "modified",
        "sort_order": "DESC",
        "states": [
            {
                "action": "Submit",
                "doc_status": 0,
                "is_optional_state": 0,
                "next_action": "Cancel",
                "next_state": "Submitted",
                "state": "Draft"
            },
            {
                "action": "Cancel",
                "doc_status": 1,
                "is_optional_state": 0,
                "next_action": "Submit",
                "next_state": "Cancelled",
                "state": "Submitted"
            },
            {
                "action": "Submit",
                "doc_status": 1,
                "is_optional_state": 0,
                "next_action": "Cancel",
                "next_state": "Submitted",
                "state": "Cancelled"
            }
        ],
        "track_changes": 1
    }
    
    with open(f"{doctype_path}/project.json", "w", encoding="utf-8") as f:
        json.dump(project_json, f, indent=2, ensure_ascii=False)
    
    # Tạo Python file với validation logic
    project_py = '''# -*- coding: utf-8 -*-
# Copyright (c) 2024, COMA and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import today, getdate, formatdate
from datetime import datetime

class Project(Document):
	def validate(self):
		self.validate_dates()
		self.validate_members()
		self.validate_budget()
		self.auto_generate_code()
	
	def validate_dates(self):
		"""Validate start and end dates"""
		if self.start_date and self.end_date:
			if getdate(self.start_date) > getdate(self.end_date):
				frappe.throw("Start Date cannot be after End Date")
	
	def validate_members(self):
		"""Validate that project has at least one member"""
		if not self.project_members:
			frappe.throw("Project must have at least one member")
		
		# Check for duplicate members
		member_names = [member.member_name for member in self.project_members]
		if len(member_names) != len(set(member_names)):
			frappe.throw("Duplicate members found in Project Members table")
	
	def validate_budget(self):
		"""Validate budget is positive"""
		if self.budget and self.budget <= 0:
			frappe.throw("Budget must be greater than 0")
	
	def auto_generate_code(self):
		"""Auto generate project code if not provided"""
		if not self.project_code:
			# Format: PRJ-YYYYMMDD-XXX
			date_str = datetime.now().strftime("%Y%m%d")
			
			# Get next sequence number for today
			existing_count = frappe.db.count("Project", {
				"project_code": ["like", f"PRJ-{date_str}-%"]
			})
			
			sequence = str(existing_count + 1).zfill(3)
			self.project_code = f"PRJ-{date_str}-{sequence}"
	
	def before_submit(self):
		"""Validation before submit"""
		if not self.project_members:
			frappe.throw("Cannot submit Project without any members")
		
		if self.status not in ["Planning", "In Progress"]:
			frappe.throw("Only Planning or In Progress projects can be submitted")
	
	def on_submit(self):
		"""Actions after submit"""
		frappe.msgprint("Project submitted successfully!")
	
	def on_cancel(self):
		"""Actions after cancel"""
		frappe.msgprint("Project cancelled!")
'''
    
    with open(f"{doctype_path}/project.py", "w", encoding="utf-8") as f:
        f.write(project_py)
    
    print(f"✅ Đã tạo: {doctype_path}/project.json")
    print(f"✅ Đã tạo: {doctype_path}/project.py")

def create_all_doctypes():
    """Tạo tất cả 3 DocTypes"""
    print("🏗️  Bắt đầu tạo DocTypes cho COMA app...")
    print()
    
    try:
        create_project_member_doctype()
        print()
        create_project_contractor_assignment_doctype()
        print()
        create_project_doctype()
        print()
        
        print("=" * 60)
        print("✅ Hoàn thành! Đã tạo 3 DocTypes:")
        print("   - Project Member (Child Table)")
        print("   - Project Contractor Assignment (Child Table)")
        print("   - Project (Master)")
        print()
        print("📋 Bước tiếp theo:")
        print("   1. Chạy: bench --site dev migrate")
        print("   2. Reload Frappe: bench --site dev reload-doctype Project")
        print("   3. Truy cập UI và test tạo Project mới")
        print("=" * 60)
        
    except Exception as e:
        print(f"❌ Lỗi khi tạo DocTypes: {str(e)}")
        raise

if __name__ == "__main__":
    create_all_doctypes()

