import frappe

def check_data():
    """Check data counts"""
    print("🔍 Checking data counts...")
    
    project_count = len(frappe.get_all("Project"))
    category_count = len(frappe.get_all("Category"))
    task_count = len(frappe.get_all("Task"))
    daily_log_count = len(frappe.get_all("Daily Log"))
    expense_count = len(frappe.get_all("Expense Entry"))
    
    print(f"Projects: {project_count}")
    print(f"Categories: {category_count}")
    print(f"Tasks: {task_count}")
    print(f"Daily Logs: {daily_log_count}")
    print(f"Expenses: {expense_count}")
    
    # Check first project details
    if project_count > 0:
        project = frappe.get_doc("Project", "DP001")
        print(f"\nFirst Project Details:")
        print(f"  Name: {project.project_name}")
        print(f"  Progress: {project.progress_percentage}%")
        print(f"  Total Expense: {project.total_expense or 0}")
    
    # Check first daily log details
    if daily_log_count > 0:
        daily_logs = frappe.get_all("Daily Log", limit=1)
        if daily_logs:
            daily_log = frappe.get_doc("Daily Log", daily_logs[0].name)
            print(f"\nFirst Daily Log Details:")
            print(f"  Name: {daily_log.name}")
            print(f"  Project: {daily_log.project}")
            print(f"  Category: {daily_log.category}")
            print(f"  Task: {daily_log.task}")
            print(f"  Fields: {list(daily_log.as_dict().keys())}")

if __name__ == "__main__":
    check_data()
