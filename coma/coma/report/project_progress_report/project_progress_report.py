# Copyright (c) 2025, Vu Linh and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters=None):
    """
    Generate Project Progress Report
    
    Returns:
        tuple: (columns, data)
    """
    columns = get_columns()
    data = get_data(filters)
    
    return columns, data


def get_columns():
    """Define report columns"""
    return [
        {
            'fieldname': 'project',
            'label': _('Project'),
            'fieldtype': 'Link',
            'options': 'Project',
            'width': 200
        },
        {
            'fieldname': 'project_status',
            'label': _('Project Status'),
            'fieldtype': 'Data',
            'width': 120
        },
        {
            'fieldname': 'category',
            'label': _('Category'),
            'fieldtype': 'Link',
            'options': 'Category',
            'width': 180
        },
        {
            'fieldname': 'category_weight',
            'label': _('Category Weight (%)'),
            'fieldtype': 'Float',
            'width': 150
        },
        {
            'fieldname': 'category_progress',
            'label': _('Category Progress (%)'),
            'fieldtype': 'Percent',
            'width': 150
        },
        {
            'fieldname': 'task',
            'label': _('Task'),
            'fieldtype': 'Link',
            'options': 'Task',
            'width': 200
        },
        {
            'fieldname': 'task_weight',
            'label': _('Task Weight (%)'),
            'fieldtype': 'Float',
            'width': 130
        },
        {
            'fieldname': 'task_status',
            'label': _('Task Status'),
            'fieldtype': 'Data',
            'width': 120
        },
        {
            'fieldname': 'task_progress',
            'label': _('Task Progress (%)'),
            'fieldtype': 'Percent',
            'width': 140
        },
        {
            'fieldname': 'assignee',
            'label': _('Assignee'),
            'fieldtype': 'Link',
            'options': 'User',
            'width': 150
        }
    ]


def get_data(filters):
    """Get report data using Frappe ORM"""
    # Get projects first
    project_filters = {}
    if filters.get('project'):
        project_filters['name'] = filters.get('project')
    if filters.get('status'):
        project_filters['status'] = filters.get('status')
    
    projects = frappe.get_all(
        'Project',
        filters=project_filters,
        fields=['name', 'status'],
        order_by='name'
    )
    
    data = []
    
    for project in projects:
        # Get categories for this project
        category_filters = {'project': project.name}
        if filters.get('category'):
            category_filters['name'] = filters.get('category')
        
        categories = frappe.get_all(
            'Category',
            filters=category_filters,
            fields=['name', 'progress_weight', 'progress_percentage', 'sort_order'],
            order_by='sort_order'
        )
        
        for category in categories:
            # Get tasks for this category
            task_filters = {'category': category.name}
            if filters.get('task_status'):
                task_filters['status'] = filters.get('task_status')
            
            tasks = frappe.get_all(
                'Task',
                filters=task_filters,
                fields=['name', 'task_weight', 'status', 'progress_percentage', 'assignee', 'sort_order'],
                order_by='sort_order'
            )
            
            if tasks:
                # Add task rows
                for task in tasks:
                    data.append({
                        'project': project.name,
                        'project_status': project.status,
                        'category': category.name,
                        'category_weight': category.progress_weight,
                        'category_progress': category.progress_percentage,
                        'task': task.name,
                        'task_weight': task.task_weight,
                        'task_status': task.status,
                        'task_progress': task.progress_percentage,
                        'assignee': task.assignee
                    })
            else:
                # Add category row without tasks
                data.append({
                    'project': project.name,
                    'project_status': project.status,
                    'category': category.name,
                    'category_weight': category.progress_weight,
                    'category_progress': category.progress_percentage,
                    'task': None,
                    'task_weight': None,
                    'task_status': None,
                    'task_progress': None,
                    'assignee': None
                })
    
    return data


def get_conditions(filters):
    """Build SQL conditions from filters"""
    conditions = ""
    
    if filters.get('project'):
        conditions += f" AND p.name = '{filters.get('project')}'"
    
    if filters.get('status'):
        conditions += f" AND p.status = '{filters.get('status')}'"
    
    if filters.get('category'):
        conditions += f" AND c.name = '{filters.get('category')}'"
    
    if filters.get('task_status'):
        conditions += f" AND t.status = '{filters.get('task_status')}'"
    
    return conditions

