import frappe

def debug_data():
    """Debug data issues"""
    print("🔍 Debugging data issues...")
    
    # Check Daily Logs
    daily_logs = frappe.get_all("Daily Log", fields=["name", "project", "category", "task"])
    print(f"Daily Logs count: {len(daily_logs)}")
    for i, log in enumerate(daily_logs[:5]):
        print(f"  {i+1}. {log.name} - {log.project} - {log.category} - {log.task}")
    
    # Check Expenses
    expenses = frappe.get_all("Expense Entry", fields=["name", "project", "amount"])
    print(f"\nExpenses count: {len(expenses)}")
    for i, exp in enumerate(expenses[:5]):
        print(f"  {i+1}. {exp.name} - {exp.project} - {exp.amount:,} VND")
    
    # Check if there are any naming issues
    print(f"\nDaily Log naming pattern check:")
    all_logs = frappe.get_all("Daily Log", fields=["name"])
    for log in all_logs:
        if "YYYY" in log.name or "MM" in log.name or "DD" in log.name or "####" in log.name:
            print(f"  Found template name: {log.name}")
    
    print(f"\nExpense naming pattern check:")
    all_expenses = frappe.get_all("Expense Entry", fields=["name"])
    for exp in all_expenses:
        if "YYYY" in exp.name or "MM" in exp.name or "DD" in exp.name or "####" in exp.name:
            print(f"  Found template name: {exp.name}")

if __name__ == "__main__":
    debug_data()
