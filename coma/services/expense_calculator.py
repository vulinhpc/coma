# Copyright (c) 2025, Vu Linh and contributors
# For license information, please see license.txt

import frappe


def calculate_project_expense(project_name):
    """
    Tính tổng chi phí project từ Expense Entry.
    
    Args:
        project_name: Name của Project document
        
    Returns:
        dict: {
            'total_expense': float,
            'total_income': float,
            'net_expense': float
        }
    """
    # Chi phí (chỉ lấy submitted entries)
    expenses = frappe.get_all(
        'Expense Entry',
        filters={
            'project': project_name,
            'docstatus': 1,  # Submitted only
            'entry_type': 'Expense'
        },
        fields=['amount']
    )
    
    # Thu nhập
    incomes = frappe.get_all(
        'Expense Entry',
        filters={
            'project': project_name,
            'docstatus': 1,
            'entry_type': 'Income'
        },
        fields=['amount']
    )
    
    total_expense = sum(e.get('amount') or 0 for e in expenses)
    total_income = sum(i.get('amount') or 0 for i in incomes)
    
    return {
        'total_expense': total_expense,
        'total_income': total_income,
        'net_expense': total_expense - total_income
    }


def update_project_expense(project_doc):
    """
    Update project total_expense field.
    
    Args:
        project_doc: Project document instance
    """
    result = calculate_project_expense(project_doc.name)
    project_doc.total_expense = result['total_expense']


def on_submit_expense(doc, method):
    """
    Hook: Khi Expense Entry được submit.
    Update project total_expense.
    
    Args:
        doc: Expense Entry document
        method: Method name (on_submit)
    """
    if doc.project:
        project = frappe.get_doc('Project', doc.project)
        update_project_expense(project)
        project.db_update()
        frappe.db.commit()


def on_cancel_expense(doc, method):
    """
    Hook: Khi Expense Entry bị cancel.
    Recalculate project total_expense.
    
    Args:
        doc: Expense Entry document
        method: Method name (on_cancel)
    """
    if doc.project:
        project = frappe.get_doc('Project', doc.project)
        update_project_expense(project)
        project.db_update()
        frappe.db.commit()

