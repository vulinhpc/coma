# Copyright (c) 2025, Vu Linh and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def validate_task_weight(doc, method):
    """
    Validate tổng task_weight trong 1 category <= 100%.
    
    Args:
        doc: Task document
        method: validate method
        
    Raises:
        frappe.ValidationError: Nếu tổng weight > 100
    """
    if not doc.category:
        return
    
    # Lấy tất cả tasks trong category (trừ task hiện tại)
    tasks = frappe.get_all(
        'Task',
        filters={
            'category': doc.category,
            'name': ['!=', doc.name]
        },
        fields=['task_weight']
    )
    
    # Tính tổng weight
    total_weight = sum(t.get('task_weight') or 0 for t in tasks)
    total_weight += doc.task_weight or 0
    
    if total_weight > 100:
        frappe.throw(
            _('Total task weight in category cannot exceed 100%. Current total: {0}%').format(total_weight)
        )


def validate_category_weight(doc, method):
    """
    Validate tổng category weight trong 1 project <= 100%.
    
    Args:
        doc: Category document
        method: validate method
        
    Raises:
        frappe.ValidationError: Nếu tổng weight > 100
    """
    if not doc.project:
        return
    
    # Lấy tất cả categories trong project (trừ category hiện tại)
    categories = frappe.get_all(
        'Category',
        filters={
            'project': doc.project,
            'name': ['!=', doc.name]
        },
        fields=['progress_weight']
    )
    
    # Tính tổng weight
    total_weight = sum(c.get('progress_weight') or 0 for c in categories)
    total_weight += doc.progress_weight or 0
    
    if total_weight > 100:
        frappe.throw(
            _('Total category weight in project cannot exceed 100%. Current total: {0}%').format(total_weight)
        )

