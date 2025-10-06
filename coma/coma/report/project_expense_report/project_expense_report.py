# Copyright (c) 2025, Vu Linh and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters=None):
    """
    Generate Project Expense Report
    
    Returns:
        tuple: (columns, data, message, chart)
    """
    columns = get_columns()
    data = get_data(filters)
    message = get_message(filters)
    chart = get_chart_data(data, filters)
    
    return columns, data, message, chart


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
            'fieldname': 'entry_date',
            'label': _('Date'),
            'fieldtype': 'Date',
            'width': 100
        },
        {
            'fieldname': 'entry_type',
            'label': _('Type'),
            'fieldtype': 'Data',
            'width': 100
        },
        {
            'fieldname': 'category_type',
            'label': _('Category'),
            'fieldtype': 'Data',
            'width': 150
        },
        {
            'fieldname': 'amount',
            'label': _('Amount'),
            'fieldtype': 'Currency',
            'width': 120
        },
        {
            'fieldname': 'description',
            'label': _('Description'),
            'fieldtype': 'Data',
            'width': 250
        },
        {
            'fieldname': 'paid_by',
            'label': _('Paid By'),
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
            ee.project,
            ee.entry_date,
            ee.entry_type,
            ee.category_type,
            ee.amount,
            ee.description,
            ee.paid_by
        FROM `tabExpense Entry` ee
        WHERE ee.docstatus = 1 {conditions}
        ORDER BY ee.entry_date DESC
    """, as_dict=1)
    
    return data


def get_conditions(filters):
    """Build SQL conditions"""
    conditions = ""
    
    if filters.get('project'):
        conditions += f" AND ee.project = '{filters.get('project')}'"
    
    if filters.get('entry_type'):
        conditions += f" AND ee.entry_type = '{filters.get('entry_type')}'"
    
    if filters.get('category_type'):
        conditions += f" AND ee.category_type = '{filters.get('category_type')}'"
    
    if filters.get('from_date'):
        conditions += f" AND ee.entry_date >= '{filters.get('from_date')}'"
    
    if filters.get('to_date'):
        conditions += f" AND ee.entry_date <= '{filters.get('to_date')}'"
    
    return conditions


def get_message(filters):
    """Get summary message"""
    if not filters.get('project'):
        return None
    
    from coma.services.expense_calculator import calculate_project_expense
    
    result = calculate_project_expense(filters.get('project'))
    project = frappe.get_doc('Project', filters.get('project'))
    
    message = f"""
    <div style="padding: 10px; background: #f8f9fa; border-radius: 5px; margin-bottom: 10px;">
        <h4>Project: {project.project_name}</h4>
        <table style="width: 100%;">
            <tr>
                <td><strong>Total Budget:</strong></td>
                <td>{frappe.format_value(project.total_budget or 0, {'fieldtype': 'Currency'})}</td>
            </tr>
            <tr>
                <td><strong>Total Expense:</strong></td>
                <td>{frappe.format_value(result['total_expense'], {'fieldtype': 'Currency'})}</td>
            </tr>
            <tr>
                <td><strong>Total Income:</strong></td>
                <td>{frappe.format_value(result['total_income'], {'fieldtype': 'Currency'})}</td>
            </tr>
            <tr>
                <td><strong>Net Expense:</strong></td>
                <td>{frappe.format_value(result['net_expense'], {'fieldtype': 'Currency'})}</td>
            </tr>
            <tr>
                <td><strong>Remaining Budget:</strong></td>
                <td>{frappe.format_value((project.total_budget or 0) - result['total_expense'], {'fieldtype': 'Currency'})}</td>
            </tr>
        </table>
    </div>
    """
    
    return message


def get_chart_data(data, filters):
    """Generate chart data"""
    if not data:
        return None
    
    # Group by category_type
    expense_by_category = {}
    
    for row in data:
        if row['entry_type'] == 'Expense':
            category = row['category_type']
            expense_by_category[category] = expense_by_category.get(category, 0) + row['amount']
    
    return {
        'data': {
            'labels': list(expense_by_category.keys()),
            'datasets': [{
                'name': 'Expense by Category',
                'values': list(expense_by_category.values())
            }]
        },
        'type': 'pie'
    }

