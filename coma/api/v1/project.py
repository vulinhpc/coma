# Copyright (c) 2025, Vu Linh and contributors
# For license information, please see license.txt

import frappe
from frappe import _


@frappe.whitelist()
def get_my_projects():
    """
    Get list of projects where current user is a team member
    
    Returns:
        list: Projects with basic info
    """
    # Get team members first
    team_members = frappe.get_all(
        'Project Team Member',
        filters={'user': frappe.session.user},
        fields=['parent'],
        order_by='modified DESC'
    )
    
    project_names = [tm.parent for tm in team_members]
    
    if project_names:
        projects = frappe.get_all(
            'Project',
            filters={'name': ['in', project_names]},
            fields=[
                'name', 'project_name', 'project_code',
                'client_name', 'status', 'progress_percentage',
                'start_date', 'end_date', 'cover_image'
            ],
            order_by='modified DESC'
        )
    else:
        projects = []
    
    return projects


@frappe.whitelist()
def get_project_details(project_id):
    """
    Get full project details with categories and tasks
    
    Args:
        project_id: Project name
        
    Returns:
        dict: {
            'project': {...},
            'categories': [{
                'category': {...},
                'tasks': [...]
            }]
        }
    """
    # Check permission
    if not has_project_access(project_id):
        frappe.throw(_('No permission to access this project'))
    
    # Get project
    project = frappe.get_doc('Project', project_id)
    
    # Get categories with tasks
    categories = frappe.get_all('Category',
                               filters={'project': project_id},
                               fields=['*'],
                               order_by='sort_order')
    
    result = []
    for cat in categories:
        tasks = frappe.get_all('Task',
                              filters={'category': cat.name},
                              fields=['*'],
                              order_by='sort_order')
        
        result.append({
            'category': cat,
            'tasks': tasks
        })
    
    return {
        'project': project.as_dict(),
        'categories': result
    }


@frappe.whitelist()
def get_category_tasks(category_id):
    """
    Get all tasks in a category
    
    Args:
        category_id: Category name
        
    Returns:
        list: Tasks
    """
    tasks = frappe.get_all('Task',
                          filters={'category': category_id},
                          fields=['*'],
                          order_by='sort_order')
    
    return tasks


@frappe.whitelist()
def submit_daily_log(data):
    """
    Submit a daily log
    
    Args:
        data: dict {
            'project': project_name,
            'category': category_name,
            'task': task_name,
            'log_date': date,
            'shift': shift,
            'work_description': text,
            'weather': weather,
            'notes': notes,
            'photos': [{'image': url, 'caption': text}]
        }
        
    Returns:
        dict: {'name': log_name, 'status': 'success'}
    """
    import json
    if isinstance(data, str):
        data = json.loads(data)
    
    # Create Daily Log
    log = frappe.get_doc({
        'doctype': 'Daily Log',
        'project': data.get('project'),
        'category': data.get('category'),
        'task': data.get('task'),
        'log_date': data.get('log_date'),
        'shift': data.get('shift'),
        'work_description': data.get('work_description'),
        'weather': data.get('weather'),
        'notes': data.get('notes')
    })
    
    # Add photos
    if data.get('photos'):
        for photo in data.get('photos'):
            log.append('photos', {
                'image': photo.get('image'),
                'caption': photo.get('caption')
            })
    
    log.insert()
    
    # Auto-submit if requested
    if data.get('auto_submit'):
        log.submit()
    
    return {
        'name': log.name,
        'status': 'success',
        'message': _('Daily Log created successfully')
    }


@frappe.whitelist()
def update_task_status(task_id, new_status):
    """
    Update task status (will trigger progress recalculation)
    
    Args:
        task_id: Task name
        new_status: Not Started / In Progress / Completed
        
    Returns:
        dict: Updated task with new progress
    """
    task = frappe.get_doc('Task', task_id)
    task.status = new_status
    task.save()
    
    # Get updated progress
    category = frappe.get_doc('Category', task.category)
    project = frappe.get_doc('Project', task.project)
    
    return {
        'task': task.as_dict(),
        'category_progress': category.progress_percentage,
        'project_progress': project.progress_percentage
    }


@frappe.whitelist()
def submit_expense(data):
    """
    Submit an expense entry
    
    Args:
        data: dict {
            'project': project_name,
            'entry_date': date,
            'entry_type': Income/Expense,
            'category_type': category,
            'amount': amount,
            'description': text,
            'receipt_image': url,
            'notes': text
        }
        
    Returns:
        dict: {'name': expense_name, 'status': 'success'}
    """
    import json
    if isinstance(data, str):
        data = json.loads(data)
    
    expense = frappe.get_doc({
        'doctype': 'Expense Entry',
        'project': data.get('project'),
        'entry_date': data.get('entry_date'),
        'entry_type': data.get('entry_type'),
        'category_type': data.get('category_type'),
        'amount': data.get('amount'),
        'description': data.get('description'),
        'receipt_image': data.get('receipt_image'),
        'notes': data.get('notes')
    })
    
    expense.insert()
    
    # Auto-submit if requested
    if data.get('auto_submit'):
        expense.submit()
    
    return {
        'name': expense.name,
        'status': 'success',
        'message': _('Expense Entry created successfully')
    }


@frappe.whitelist()
def get_project_summary(project_id):
    """
    Get project summary (progress + expense + recent logs)
    
    Args:
        project_id: Project name
        
    Returns:
        dict: {
            'progress': {...},
            'expense': {...},
            'recent_logs': [...]
        }
    """
    from coma.services.progress_calculator import calculate_project_progress
    from coma.services.expense_calculator import calculate_project_expense
    
    # Check permission
    if not has_project_access(project_id):
        frappe.throw(_('No permission to access this project'))
    
    project = frappe.get_doc('Project', project_id)
    
    # Progress summary
    categories = frappe.get_all('Category',
                               filters={'project': project_id},
                               fields=['name', 'category_name', 'progress_percentage', 'status'])
    
    # Expense summary
    expense_data = calculate_project_expense(project_id)
    
    # Recent logs
    recent_logs = frappe.get_all('Daily Log',
                                filters={'project': project_id},
                                fields=['name', 'log_date', 'task', 'work_description', 'docstatus'],
                                order_by='log_date DESC',
                                limit=10)
    
    return {
        'progress': {
            'percentage': project.progress_percentage,
            'categories': categories
        },
        'expense': {
            'budget': project.total_budget,
            'actual': expense_data.get('total_expense'),
            'income': expense_data.get('total_income'),
            'remaining': (project.total_budget or 0) - expense_data.get('total_expense', 0)
        },
        'recent_logs': recent_logs
    }


def has_project_access(project_id):
    """
    Check if current user has access to project
    
    Args:
        project_id: Project name
        
    Returns:
        bool: True if has access
    """
    if frappe.session.user == 'Administrator':
        return True
    
    # Check if user is team member using Frappe ORM
    members = frappe.get_all(
        'Project Team Member',
        filters={
            'parent': project_id,
            'user': frappe.session.user
        },
        limit=1
    )
    
    return len(members) > 0

