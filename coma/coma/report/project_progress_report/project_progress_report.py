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
    """Get report data"""
    conditions = get_conditions(filters)
    
    data = frappe.db.sql(f"""
        SELECT
            p.name as project,
            p.status as project_status,
            c.name as category,
            c.progress_weight as category_weight,
            c.progress_percentage as category_progress,
            t.name as task,
            t.task_weight as task_weight,
            t.status as task_status,
            t.progress_percentage as task_progress,
            t.assignee
        FROM `tabProject` p
        LEFT JOIN `tabCategory` c ON c.project = p.name
        LEFT JOIN `tabTask` t ON t.category = c.name
        WHERE 1=1 {conditions}
        ORDER BY p.name, c.sort_order, t.sort_order
    """, as_dict=1)
    
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

