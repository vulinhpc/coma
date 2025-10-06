import frappe, json, os

def sync_all_workspace_content():
    """
    Đồng bộ toàn bộ nội dung layout (content[]) của các workspace 
    từ JSON fixture vào database để dashboard hiển thị đầy đủ.
    """
    print("🔄 Starting workspace content sync...")
    
    workspace_path = os.path.join(frappe.get_app_path("coma"), "coma", "workspace")
    synced = []
    
    # Lấy danh sách tất cả thư mục workspace
    if not os.path.exists(workspace_path):
        print("❌ Workspace path not found:", workspace_path)
        return
    
    for folder in os.listdir(workspace_path):
        folder_path = os.path.join(workspace_path, folder)
        json_file = os.path.join(folder_path, f"{folder}.json")
        
        if os.path.exists(json_file):
            try:
                with open(json_file, 'r') as f:
                    data = json.load(f)
                
                name = data.get("name")
                content = data.get("content", [])
                print(f"  Reading {folder}: name={name}, content_type={type(content)}, content_len={len(content) if isinstance(content, list) else 'not_list'}")
                
                if name and frappe.db.exists("Workspace", name):
                    doc = frappe.get_doc("Workspace", name)
                    
                    # Cập nhật content từ JSON
                    if content:
                        # Content phải là string JSON
                        if isinstance(content, list):
                            content_json = json.dumps(content)
                        else:
                            content_json = content
                        
                        doc.content = content_json
                        doc.save(ignore_permissions=True, ignore_version=True)
                        synced.append(name)
                        print(f"✅ Synced workspace content: {name}")
                        print(f"   Content length: {len(content_json)} characters")
                    else:
                        print(f"⚠️  No content found for workspace: {name}")
                else:
                    print(f"❌ Workspace not found in DB: {name}")
                    
            except Exception as e:
                print(f"❌ Error syncing {folder}: {str(e)}")
    
    # Note: frappe.db.commit() removed as it's not needed for save operations
    print(f"🎯 All workspace contents synced successfully: {', '.join(synced)}")
    print(f"📊 Total synced: {len(synced)} workspaces")
    
    return synced

if __name__ == "__main__":
    sync_all_workspace_content()
