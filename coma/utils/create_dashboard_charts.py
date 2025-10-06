import frappe

def create_dashboard_charts():
    """Create dashboard charts for COMA workspaces"""
    
    print("📊 Creating dashboard charts...")
    
    # Chart 1: Project Progress Overview
    try:
        chart1 = frappe.get_doc({
            "doctype": "Dashboard Chart",
            "chart_name": "Project Progress Overview",
            "chart_type": "Report",
            "report_name": "Project Progress Report",
            "type": "Donut",
            "timespan": "Last Month",
            "module": "COMA",
            "is_public": 1,
            "use_report_chart": 1,
            "filters_json": "{}"
        })
        chart1.insert(ignore_if_duplicate=True)
        print("   ✅ Created: Project Progress Overview")
    except Exception as e:
        print(f"   ❌ Error creating Project Progress Overview: {str(e)}")
    
    # Chart 2: Expense Summary
    try:
        chart2 = frappe.get_doc({
            "doctype": "Dashboard Chart",
            "chart_name": "Expense Summary",
            "chart_type": "Report",
            "report_name": "Project Expense Report",
            "type": "Bar",
            "timespan": "Last Month",
            "module": "COMA",
            "is_public": 1,
            "use_report_chart": 1,
            "filters_json": "{}"
        })
        chart2.insert(ignore_if_duplicate=True)
        print("   ✅ Created: Expense Summary")
    except Exception as e:
        print(f"   ❌ Error creating Expense Summary: {str(e)}")
    
    # Chart 3: Daily Log Activity
    try:
        chart3 = frappe.get_doc({
            "doctype": "Dashboard Chart",
            "chart_name": "Daily Log Activity",
            "chart_type": "Count",
            "based_on": "creation",
            "document_type": "Daily Log",
            "type": "Line",
            "timespan": "Last Week",
            "module": "COMA",
            "is_public": 1,
            "filters_json": "{}"
        })
        chart3.insert(ignore_if_duplicate=True)
        print("   ✅ Created: Daily Log Activity")
    except Exception as e:
        print(f"   ❌ Error creating Daily Log Activity: {str(e)}")
    
    # Chart 4: Project Budget Overview
    try:
        chart4 = frappe.get_doc({
            "doctype": "Dashboard Chart",
            "chart_name": "Project Budget Overview",
            "chart_type": "Report",
            "report_name": "Project Expense Report",
            "type": "Pie",
            "timespan": "Last Month",
            "module": "COMA",
            "is_public": 1,
            "use_report_chart": 1,
            "filters_json": "{}"
        })
        chart4.insert(ignore_if_duplicate=True)
        print("   ✅ Created: Project Budget Overview")
    except Exception as e:
        print(f"   ❌ Error creating Project Budget Overview: {str(e)}")
    
    # Chart 5: User Activity
    try:
        chart5 = frappe.get_doc({
            "doctype": "Dashboard Chart",
            "chart_name": "User Activity",
            "chart_type": "Count",
            "based_on": "creation",
            "document_type": "User",
            "type": "Bar",
            "timespan": "Last Month",
            "module": "COMA",
            "is_public": 1,
            "filters_json": "{}"
        })
        chart5.insert(ignore_if_duplicate=True)
        print("   ✅ Created: User Activity")
    except Exception as e:
        print(f"   ❌ Error creating User Activity: {str(e)}")
    
    # Note: frappe.db.commit() removed as it's not needed for insert operations
    print("✅ Dashboard charts creation completed!")

if __name__ == "__main__":
    create_dashboard_charts()
