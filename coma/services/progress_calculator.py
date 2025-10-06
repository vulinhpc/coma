# Copyright (c) 2025, Vu Linh and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def calculate_task_progress(task):
    """
    Tính tiến độ task dựa trên status.
    
    Args:
        task: Task document hoặc dict with 'status' field
        
    Returns:
        float: Progress percentage (0, 50, or 100)
    """
    status_map = {
        'Not Started': 0,
        'In Progress': 50,
        'Completed': 100
    }
    
    if isinstance(task, dict):
        status = task.get('status')
    else:
        status = task.status
        
    return status_map.get(status, 0)


def calculate_category_progress(category_name):
    """
    Tính tiến độ category = weighted average của tasks.
    Nếu không có task_weight, dùng simple average.
    
    Args:
        category_name: Name của Category document
        
    Returns:
        float: Progress percentage (0-100)
    """
    tasks = frappe.get_all(
        'Task',
        filters={'category': category_name},
        fields=['name', 'task_weight', 'status']
    )
    
    if not tasks:
        return 0
    
    # Tính tổng weight
    total_weight = sum(t.get('task_weight') or 0 for t in tasks)
    
    if total_weight == 0:
        # Simple average nếu không có weight
        total_progress = sum(calculate_task_progress(t) for t in tasks)
        return total_progress / len(tasks)
    else:
        # Weighted average
        weighted_progress = sum(
            calculate_task_progress(t) * (t.get('task_weight') or 0)
            for t in tasks
        )
        return weighted_progress / total_weight


def calculate_project_progress(project_name):
    """
    Tính tiến độ project = weighted average của categories.
    
    Args:
        project_name: Name của Project document
        
    Returns:
        float: Progress percentage (0-100)
    """
    categories = frappe.get_all(
        'Category',
        filters={'project': project_name},
        fields=['name', 'progress_weight']
    )
    
    if not categories:
        return 0
    
    total_weight = sum(c.get('progress_weight') or 0 for c in categories)
    
    if total_weight == 0:
        # Simple average
        total_progress = sum(
            calculate_category_progress(c.name)
            for c in categories
        )
        return total_progress / len(categories)
    else:
        # Weighted average
        weighted_progress = sum(
            calculate_category_progress(c.name) * (c.get('progress_weight') or 0)
            for c in categories
        )
        return weighted_progress / total_weight


def update_task_progress(task_doc):
    """
    Update task progress percentage.
    
    Args:
        task_doc: Task document instance
    """
    task_doc.progress_percentage = calculate_task_progress(task_doc)


def update_category_progress(category_doc):
    """
    Update category progress percentage.
    
    Args:
        category_doc: Category document instance
    """
    category_doc.progress_percentage = calculate_category_progress(category_doc.name)


def update_project_progress(project_doc):
    """
    Update project progress percentage.
    
    Args:
        project_doc: Project document instance
    """
    project_doc.progress_percentage = calculate_project_progress(project_doc.name)


def recalculate_all_progress(project_name):
    """
    Recalculate toàn bộ progress của project.
    Gọi khi cần sync lại tất cả (ví dụ: sau khi import data).
    
    Args:
        project_name: Name của Project document
    """
    # Update all tasks
    tasks = frappe.get_all('Task', filters={'project': project_name})
    for task in tasks:
        task_doc = frappe.get_doc('Task', task.name)
        update_task_progress(task_doc)
        task_doc.db_update()
    
    # Update all categories
    categories = frappe.get_all('Category', filters={'project': project_name})
    for cat in categories:
        cat_doc = frappe.get_doc('Category', cat.name)
        update_category_progress(cat_doc)
        cat_doc.db_update()
    
    # Update project
    project_doc = frappe.get_doc('Project', project_name)
    update_project_progress(project_doc)
    project_doc.db_update()
    
    frappe.msgprint(_('Progress recalculated successfully for project {0}').format(project_name))

