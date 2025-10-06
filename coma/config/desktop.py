# Copyright (c) 2025, Vu Linh and contributors
# For license information, please see license.txt

from frappe import _


def get_data():
    return [
        {
            "module_name": "COMA",
            "color": "blue",
            "icon": "fa fa-building",
            "type": "module",
            "label": _("COMA"),
        }
    ]


def get_workspace_sidebar_items():
    """
    Return sidebar items for COMA workspace
    """
    return {
        "COMA": {
            "label": _("Construction Management"),
            "items": [
                # Projects Section
                {
                    "type": "Card Break",
                    "label": _("Projects")
                },
                {
                    "type": "Link",
                    "name": "Project",
                    "label": _("Projects"),
                    "description": _("Manage construction projects"),
                    "onboard": 1
                },
                {
                    "type": "Link",
                    "name": "Category",
                    "label": _("Categories"),
                    "description": _("Project categories/phases"),
                    "dependencies": ["Project"]
                },
                {
                    "type": "Link",
                    "name": "Task",
                    "label": _("Tasks"),
                    "description": _("Work items and assignments"),
                    "dependencies": ["Category"]
                },
                
                # Daily Operations Section
                {
                    "type": "Card Break",
                    "label": _("Daily Operations")
                },
                {
                    "type": "Link",
                    "name": "Daily Log",
                    "label": _("Daily Logs"),
                    "description": _("Daily work progress reports"),
                    "dependencies": ["Task"]
                },
                {
                    "type": "Link",
                    "name": "Expense Entry",
                    "label": _("Expenses"),
                    "description": _("Income and expense tracking"),
                    "dependencies": ["Project"]
                },
                
                # Reports Section
                {
                    "type": "Card Break",
                    "label": _("Reports")
                },
                {
                    "type": "Link",
                    "name": "Project Progress Report",
                    "label": _("Progress Report"),
                    "description": _("View project progress"),
                    "is_query_report": 1
                },
                {
                    "type": "Link",
                    "name": "Project Expense Report",
                    "label": _("Expense Report"),
                    "description": _("View project expenses"),
                    "is_query_report": 1
                },
                
                # Settings Section
                {
                    "type": "Card Break",
                    "label": _("Settings")
                },
                {
                    "type": "Link",
                    "name": "User",
                    "label": _("Users"),
                    "description": _("Manage system users")
                }
            ]
        }
    }