import frappe

def test_reports():
    """Test COMA reports"""
    print("📈 Testing COMA Reports...")
    
    try:
        # Test Project Progress Report
        print("\n📊 Project Progress Report:")
        from coma.coma.report.project_progress_report.project_progress_report import execute
        progress_data = execute(frappe._dict({"filters": {"project": "DP001"}}))
        print(f"   Columns: {progress_data[0]}")
        print(f"   Rows: {len(progress_data[1])}")
        if len(progress_data[1]) > 0:
            print(f"   Sample data: {progress_data[1][0]}")
            print("   ✅ PASS: Progress report working")
        else:
            print("   ❌ FAIL: No data in progress report")
            
    except Exception as e:
        print(f"   ❌ ERROR: {str(e)}")
    
    try:
        # Test Project Expense Report
        print("\n💰 Project Expense Report:")
        from coma.coma.report.project_expense_report.project_expense_report import execute
        expense_data = execute(frappe._dict({"filters": {"project": "DP001"}}))
        print(f"   Columns: {expense_data[0]}")
        print(f"   Rows: {len(expense_data[1])}")
        if len(expense_data[1]) > 0:
            print(f"   Sample data: {expense_data[1][0]}")
            print("   ✅ PASS: Expense report working")
        else:
            print("   ❌ FAIL: No data in expense report")
            
    except Exception as e:
        print(f"   ❌ ERROR: {str(e)}")
    
    # Test workspace access
    print("\n🏠 Workspace Access:")
    try:
        workspaces = frappe.get_all("Workspace", filters={"module": "COMA"})
        print(f"   COMA Workspaces: {len(workspaces)}")
        for ws in workspaces:
            print(f"   - {ws.name}")
        print("   ✅ PASS: Workspaces accessible")
    except Exception as e:
        print(f"   ❌ ERROR: {str(e)}")

if __name__ == "__main__":
    test_reports()
