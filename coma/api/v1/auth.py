# Copyright (c) 2025, Vu Linh and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.auth import LoginManager


@frappe.whitelist(allow_guest=True)
def login(usr, pwd):
    """
    API Login endpoint
    
    Args:
        usr: Email/Username
        pwd: Password
        
    Returns:
        dict: {
            'message': 'Logged in',
            'user': user_email,
            'full_name': full_name,
            'api_key': api_key,
            'api_secret': api_secret
        }
    """
    try:
        login_manager = LoginManager()
        login_manager.authenticate(usr, pwd)
        login_manager.post_login()
        
        # Generate API keys
        user = frappe.get_doc('User', frappe.session.user)
        api_key = user.api_key
        api_secret = frappe.generate_hash(length=15)
        
        if not api_key:
            api_key = frappe.generate_hash(length=15)
            user.api_key = api_key
        
        user.api_secret = api_secret
        user.save(ignore_permissions=True)
        
        return {
            'message': 'Logged in',
            'user': frappe.session.user,
            'full_name': user.full_name,
            'api_key': api_key,
            'api_secret': api_secret
        }
    except frappe.exceptions.AuthenticationError:
        frappe.clear_messages()
        frappe.local.response['message'] = 'Invalid credentials'
        return None


@frappe.whitelist()
def logout():
    """
    API Logout endpoint
    
    Returns:
        dict: {'message': 'Logged out'}
    """
    frappe.local.login_manager.logout()
    frappe.db.commit()
    
    return {'message': 'Logged out'}


@frappe.whitelist()
def get_user_profile():
    """
    Get current user profile and assigned projects
    
    Returns:
        dict: {
            'user': user_email,
            'full_name': full_name,
            'projects': [list of projects]
        }
    """
    user = frappe.get_doc('User', frappe.session.user)
    
    # Get projects where user is a team member
    projects = frappe.db.sql("""
        SELECT DISTINCT p.name, p.project_name, p.status, p.cover_image
        FROM `tabProject` p
        INNER JOIN `tabProject Team Member` ptm ON ptm.parent = p.name
        WHERE ptm.user = %s
        ORDER BY p.modified DESC
    """, (frappe.session.user,), as_dict=True)
    
    return {
        'user': user.email,
        'full_name': user.full_name,
        'user_image': user.user_image,
        'projects': projects
    }

