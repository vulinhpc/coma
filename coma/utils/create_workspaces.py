import frappe, json, os

def create_workspaces_from_json():
    """Tạo workspace từ JSON files"""
    print("🔄 Creating workspaces from JSON files...")
    
    workspace_path = os.path.join(frappe.get_app_path("coma"), "coma", "workspace")
    created = []
    
    for folder in os.listdir(workspace_path):
        folder_path = os.path.join(workspace_path, folder)
        json_file = os.path.join(folder_path, f"{folder}.json")
        
        if os.path.exists(json_file):
            try:
                with open(json_file, "r") as f:
                    data = json.load(f)
                
                name = data.get("name")
                if name and not frappe.db.exists("Workspace", name):
                    # Tạo workspace mới
                    doc = frappe.get_doc(data)
                    doc.insert(ignore_permissions=True)
                    created.append(name)
                    print(f"✅ Created workspace: {name}")
                else:
                    print(f"⚠️  Workspace {name} already exists or no name found")
                    
            except Exception as e:
                print(f"❌ Error creating {folder}: {str(e)}")
    
    # Note: frappe.db.commit() removed as it's not needed for insert operations
    print(f"🎯 Created {len(created)} workspaces: {created}")
    return created

if __name__ == "__main__":
    create_workspaces_from_json()
