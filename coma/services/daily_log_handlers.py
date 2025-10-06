# Copyright (c) 2025, Vu Linh and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import now


def before_save_daily_log(doc, method):
    """
    Hook: Trước khi save Daily Log.
    Auto-fill created_by field.
    
    Args:
        doc: Daily Log document
        method: before_save
    """
    if not doc.created_by:
        doc.created_by = frappe.session.user


def on_submit_daily_log(doc, method):
    """
    Hook: Khi Daily Log được submit.
    - Set submitted_at = now
    - Nếu có approved_by, set approved_at = now
    
    Args:
        doc: Daily Log document
        method: on_submit
    """
    # Set submitted_at
    doc.db_set('submitted_at', now(), update_modified=False)
    
    # Nếu có approved_by, set approved_at
    if doc.approved_by:
        doc.db_set('approved_at', now(), update_modified=False)

