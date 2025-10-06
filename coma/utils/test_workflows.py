import frappe

def test_workflows():
    """Test COMA workflows end-to-end"""
    
    print("🧪 Starting COMA workflow tests...")
    
    # === TEST 1: PROGRESS CALCULATION ===
    print("\n📊 TEST 1: Progress Calculation")
    try:
        # Get first project
        project = frappe.get_doc("Project", "DP001")
        print(f"   Project: {project.project_name}")
        print(f"   Initial Progress: {project.progress_percentage}%")
        
        # Get first task and change status to Completed
        task = frappe.get_doc("Task", "TASK-DP001-01-01")
        print(f"   Task: {task.task_name}")
        print(f"   Initial Status: {task.status}")
        
        # Change task status to Completed
        task.status = "Completed"
        task.save()
        print(f"   Updated Status: {task.status}")
        
        # Check if project progress updated
        project.reload()
        print(f"   Updated Project Progress: {project.progress_percentage}%")
        
        if project.progress_percentage > 0:
            print("   ✅ PASS: Progress calculation working")
        else:
            print("   ❌ FAIL: Progress not updated")
            
    except Exception as e:
        print(f"   ❌ ERROR: {str(e)}")
    
    # === TEST 2: EXPENSE TRACKING ===
    print("\n💰 TEST 2: Expense Tracking")
    try:
        # Get first project
        project = frappe.get_doc("Project", "DP001")
        print(f"   Project: {project.project_name}")
        print(f"   Initial Total Expense: {project.total_expense or 0:,} VND")
        
        # Get project expenses
        expenses = frappe.get_all("Expense Entry", 
                                filters={"project": project.name},
                                fields=["name", "amount", "entry_type"])
        
        total_expense = sum(exp.amount for exp in expenses if exp.entry_type == "Expense")
        total_income = sum(exp.amount for exp in expenses if exp.entry_type == "Income")
        net_expense = total_expense - total_income
        
        print(f"   Calculated Total Expense: {total_expense:,} VND")
        print(f"   Calculated Total Income: {total_income:,} VND")
        print(f"   Calculated Net Expense: {net_expense:,} VND")
        
        # Check if project total_expense matches
        project.reload()
        if abs(project.total_expense - net_expense) < 1:  # Allow small rounding difference
            print("   ✅ PASS: Expense tracking working")
        else:
            print(f"   ❌ FAIL: Project total_expense ({project.total_expense:,}) != calculated ({net_expense:,})")
            
    except Exception as e:
        print(f"   ❌ ERROR: {str(e)}")
    
    # === TEST 3: DAILY LOG WORKFLOW ===
    print("\n📝 TEST 3: Daily Log Workflow")
    try:
        # Get first daily log
        daily_log = frappe.get_doc("Daily Log", frappe.get_all("Daily Log", limit=1)[0].name)
        print(f"   Daily Log: {daily_log.name}")
        print(f"   Project: {daily_log.project}")
        print(f"   Category: {daily_log.category}")
        print(f"   Task: {daily_log.task}")
        print(f"   Description: {daily_log.work_description}")
        
        # Verify links are working
        if daily_log.project and daily_log.category and daily_log.task:
            print("   ✅ PASS: Daily log links working")
        else:
            print("   ❌ FAIL: Daily log links missing")
            
    except Exception as e:
        print(f"   ❌ ERROR: {str(e)}")
    
    # === TEST 4: REPORTS DATA ===
    print("\n📈 TEST 4: Reports Data")
    try:
        # Test Project Progress Report
        from coma.coma.report.project_progress_report.project_progress_report import execute
        progress_data = execute(frappe._dict({"filters": {"project": "DP001"}}))
        print(f"   Progress Report Rows: {len(progress_data[1])}")
        
        # Test Project Expense Report
        from coma.coma.report.project_expense_report.project_expense_report import execute
        expense_data = execute(frappe._dict({"filters": {"project": "DP001"}}))
        print(f"   Expense Report Rows: {len(expense_data[1])}")
        
        if len(progress_data[1]) > 0 and len(expense_data[1]) > 0:
            print("   ✅ PASS: Reports generating data")
        else:
            print("   ❌ FAIL: Reports not generating data")
            
    except Exception as e:
        print(f"   ❌ ERROR: {str(e)}")
    
    # === TEST 5: DATA INTEGRITY ===
    print("\n🔍 TEST 5: Data Integrity")
    try:
        # Count all records
        project_count = len(frappe.get_all("Project"))
        category_count = len(frappe.get_all("Category"))
        task_count = len(frappe.get_all("Task"))
        daily_log_count = len(frappe.get_all("Daily Log"))
        expense_count = len(frappe.get_all("Expense Entry"))
        
        print(f"   Projects: {project_count}")
        print(f"   Categories: {category_count}")
        print(f"   Tasks: {task_count}")
        print(f"   Daily Logs: {daily_log_count}")
        print(f"   Expenses: {expense_count}")
        
        expected_counts = {"Projects": 3, "Categories": 15, "Tasks": 90, "Daily Logs": 180, "Expenses": 30}
        actual_counts = {"Projects": project_count, "Categories": category_count, "Tasks": task_count, "Daily Logs": daily_log_count, "Expenses": expense_count}
        
        all_correct = True
        for key, expected in expected_counts.items():
            if actual_counts[key] != expected:
                print(f"   ❌ {key}: Expected {expected}, Got {actual_counts[key]}")
                all_correct = False
        
        if all_correct:
            print("   ✅ PASS: All data counts correct")
        else:
            print("   ❌ FAIL: Data count mismatch")
            
    except Exception as e:
        print(f"   ❌ ERROR: {str(e)}")
    
    print("\n🎯 Workflow testing completed!")

if __name__ == "__main__":
    test_workflows()
