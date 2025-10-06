import frappe, random, datetime, time

def seed_demo_data():
    """Seed demo data for COMA MVP testing"""
    
    print("🚀 Starting COMA demo data seeding...")
    
    # === CLEAR OLD DATA ===
    print("🧹 Clearing old data...")
    for doctype in ["Daily Log", "Task", "Category", "Project", "Expense Entry"]:
        try:
            # Use frappe.delete_doc instead of frappe.db.delete
            docs = frappe.get_all(doctype, fields=["name"])
            for doc in docs:
                frappe.delete_doc(doctype, doc.name, ignore_permissions=True, force=True)
            print(f"   ✅ Cleared {doctype}")
        except Exception as e:
            print(f"   ⚠️  {doctype}: {str(e)}")
    
    # Note: frappe.db.commit() removed as it's not needed for delete_doc
    print("✅ Old data cleared successfully")

    # === PROJECTS ===
    print("🏗️  Creating projects...")
    projects = []
    for i in range(3):
        project = frappe.get_doc({
            "doctype": "Project",
            "project_code": f"DP{i+1:03d}",
            "project_name": f"Demo Project {i+1}",
            "client_name": f"Demo Client {i+1}",
            "status": "In Progress",
            "start_date": datetime.date.today(),
            "end_date": datetime.date.today() + datetime.timedelta(days=30),
            "progress_percentage": 0
        }).insert()
        projects.append(project)
        print(f"   ✅ Created Project: {project.project_name}")

        # === CATEGORIES ===
        print(f"📂 Creating categories for {project.project_name}...")
        categories = []
        for j in range(5):
            category = frappe.get_doc({
                "doctype": "Category",
                "name": f"CAT-{project.project_code}-{j+1:02d}",
                "category_name": f"Category {j+1} - {project.project_name}",
                "project": project.name,
                "progress_weight": 20
            }).insert()
            categories.append(category)
            print(f"   ✅ Created Category: {category.category_name}")

            # === TASKS ===
            print(f"📋 Creating tasks for {category.category_name}...")
            tasks = []
            # Ensure total weight = 100% (6 tasks: 20, 20, 20, 20, 10, 10)
            task_weights = [20, 20, 20, 20, 10, 10]
            for k in range(6):
                task = frappe.get_doc({
                    "doctype": "Task",
                    "name": f"TASK-{project.project_code}-{j+1:02d}-{k+1:02d}",
                    "task_name": f"Task {k+1} - {category.category_name}",
                    "project": project.name,
                    "category": category.name,
                    "status": random.choice(["Not Started", "In Progress", "Completed"]),
                    "task_weight": task_weights[k]
                }).insert()
                tasks.append(task)
                print(f"   ✅ Created Task: {task.task_name}")

                # === DAILY LOGS ===
                print(f"📝 Creating daily logs for {task.task_name}...")
                for l in range(2):
                    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
                    time.sleep(0.001)  # Small delay to ensure unique timestamp
                    daily_log = frappe.get_doc({
                        "doctype": "Daily Log",
                        "project": project.name,
                        "category": category.name,
                        "task": task.name,
                        "log_date": datetime.date.today(),
                        "work_description": f"Work done on {task.task_name} - Day {l+1}",
                        "weather": random.choice(["Sunny", "Cloudy", "Rainy"])
                    })
                    daily_log.insert(ignore_if_duplicate=True)
                    print(f"   ✅ Created Daily Log: {daily_log.name}")

        # === EXPENSES ===
        print(f"💰 Creating expenses for {project.project_name}...")
        for m in range(10):
            expense = frappe.get_doc({
                "doctype": "Expense Entry",
                "project": project.name,
                "entry_date": datetime.date.today(),
                "entry_type": random.choice(["Expense", "Income"]),
                "amount": random.randint(500000, 5000000),
                "description": f"Expense item {m+1} for {project.project_name}"
            })
            expense.insert(ignore_if_duplicate=True)
            print(f"   ✅ Created Expense: {expense.name} - {expense.amount:,} VND")

    # Note: frappe.db.commit() removed as it's not needed for insert operations
    
    # === SUMMARY ===
    print("\n📊 SEED DATA SUMMARY:")
    print(f"   🏗️  Projects: {len(projects)}")
    print(f"   📂 Categories: {len(projects) * 5}")
    print(f"   📋 Tasks: {len(projects) * 5 * 6}")
    print(f"   📝 Daily Logs: {len(projects) * 5 * 6 * 2}")
    print(f"   💰 Expenses: {len(projects) * 10}")
    
    return "✅ Seed demo data completed successfully!"

if __name__ == "__main__":
    seed_demo_data()
