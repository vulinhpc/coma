import frappe

def create_workspace(name, label, shortcuts=[], charts=[], links=[]):
    """Create workspace using Frappe v15 Block System"""
    ws = frappe.new_doc("Workspace")
    ws.name = name
    ws.title = label
    ws.label = label
    ws.public = 1
    ws.module = "COMA"
    
    # Add shortcuts
    for s in shortcuts:
        ws.append("shortcuts", s)
    
    # Add charts
    for c in charts:
        ws.append("charts", c)
    
    # Add links
    for l in links:
        ws.append("links", l)
    
    ws.insert(ignore_permissions=True)
    frappe.db.commit()
    print(f"✅ Created workspace: {name}")

def migrate_all_workspaces():
    """Migrate all COMA workspaces to Block System"""
    print("🔄 Starting workspace migration to Block System...")
    
    # Construction Management - Main workspace with shortcuts and charts
    create_workspace(
        name="Construction Management",
        label="Construction Management",
        shortcuts=[
            {"link_to": "Project", "label": "Projects"},
            {"link_to": "Daily Log", "label": "Daily Logs"},
            {"link_to": "Expense Entry", "label": "Finance"},
        ],
        charts=[
            {"chart": "Project Progress"}
        ]
    )
    
    # Other workspaces - Basic structure
    create_workspace("Projects", "Projects", [], [])
    create_workspace("Daily Logs", "Daily Logs", [], [])
    create_workspace("Finance", "Finance", [], [])
    create_workspace("Reports", "Reports", [], [])
    create_workspace("Settings", "Settings", [], [])
    
    print("🎯 All workspaces migrated successfully to Block System!")

if __name__ == "__main__":
    migrate_all_workspaces()
