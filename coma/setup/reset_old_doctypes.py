#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Reset old DocTypes để bắt đầu lại theo spec MVP mới
"""

import frappe

def reset_old_doctypes():
    print("🔄 Bắt đầu reset các DocTypes cũ...")
    
    # Danh sách DocTypes cũ cần xóa
    old_doctypes = [
        "Project",
        "Project Member", 
        "Project Contractor Assignment"
    ]
    
    print(f"📋 DocTypes cũ cần xóa: {old_doctypes}")
    
    for doctype_name in old_doctypes:
        try:
            print(f"\n🗑️  Đang xóa DocType: {doctype_name}")
            
            # Kiểm tra DocType có tồn tại không
            if frappe.db.exists("DocType", doctype_name):
                # Xóa tất cả records trước
                frappe.db.sql(f"DELETE FROM `tab{doctype_name}`")
                print(f"   ✅ Đã xóa tất cả records của {doctype_name}")
                
                # Xóa DocType
                frappe.delete_doc("DocType", doctype_name, force=True)
                print(f"   ✅ Đã xóa DocType {doctype_name}")
                
                # Drop table
                frappe.db.sql(f"DROP TABLE IF EXISTS `tab{doctype_name}`")
                print(f"   ✅ Đã drop table tab{doctype_name}")
                
            else:
                print(f"   ⚠️  DocType {doctype_name} không tồn tại")
                
        except Exception as e:
            print(f"   ❌ Lỗi khi xóa {doctype_name}: {str(e)}")
    
    # Commit changes
    frappe.db.commit()
    print("\n✅ Hoàn thành reset DocTypes cũ!")
    
    # Kiểm tra kết quả
    print("\n📊 Kiểm tra kết quả:")
    remaining_doctypes = frappe.get_all("DocType", filters={"module": "COMA"})
    print(f"DocTypes còn lại trong module COMA: {len(remaining_doctypes)}")
    for dt in remaining_doctypes:
        print(f"  - {dt.name}")

if __name__ == "__main__":
    reset_old_doctypes()

