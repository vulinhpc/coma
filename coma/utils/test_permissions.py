import frappe

def test_permissions():
    """Test COMA permissions"""
    print("🔐 Testing COMA Permissions...")
    
    try:
        # Check current user
        current_user = frappe.session.user
        print(f"   Current User: {current_user}")
        
        # Check user roles
        user_roles = frappe.get_roles()
        print(f"   User Roles: {user_roles}")
        
        # Test DocType permissions
        print("\n📋 DocType Permissions:")
        doctypes = ["Project", "Category", "Task", "Daily Log", "Expense Entry"]
        
        for doctype in doctypes:
            try:
                # Test read permission
                can_read = frappe.has_permission(doctype, "read")
                can_write = frappe.has_permission(doctype, "write")
                can_create = frappe.has_permission(doctype, "create")
                can_delete = frappe.has_permission(doctype, "delete")
                
                print(f"   {doctype}:")
                print(f"     Read: {'✅' if can_read else '❌'}")
                print(f"     Write: {'✅' if can_write else '❌'}")
                print(f"     Create: {'✅' if can_create else '❌'}")
                print(f"     Delete: {'✅' if can_delete else '❌'}")
                
            except Exception as e:
                print(f"   {doctype}: ❌ ERROR - {str(e)}")
        
        # Test workspace permissions
        print("\n🏠 Workspace Permissions:")
        try:
            workspaces = frappe.get_all("Workspace", filters={"module": "COMA"})
            for ws in workspaces:
                can_access = frappe.has_permission("Workspace", "read", ws.name)
                print(f"   {ws.name}: {'✅' if can_access else '❌'}")
        except Exception as e:
            print(f"   ❌ ERROR: {str(e)}")
        
        print("\n✅ Permission testing completed!")
        
    except Exception as e:
        print(f"❌ ERROR: {str(e)}")

if __name__ == "__main__":
    test_permissions()
