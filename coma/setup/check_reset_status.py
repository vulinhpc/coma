#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kiểm tra trạng thái sau khi reset DocTypes
"""

import frappe

def check_reset_status():
    print("=== Kiểm tra DocTypes sau reset ===")
    
    doctypes = frappe.get_all("DocType", filters={"module": "COMA"})
    print(f"DocTypes trong module COMA: {len(doctypes)}")
    
    for dt in doctypes:
        print(f"  - {dt.name}")
    
    if len(doctypes) == 0:
        print("✅ Hệ thống đã sạch, sẵn sàng tạo DocTypes mới!")
    else:
        print("⚠️  Vẫn còn DocTypes cũ, cần xóa thêm")
    
    print("\n=== Kiểm tra thư mục doctype ===")
    import os
    doctype_path = "/home/lroot/frappe-bench/apps/coma/coma/coma/doctype"
    if os.path.exists(doctype_path):
        files = os.listdir(doctype_path)
        print(f"Files trong doctype folder: {files}")
        if len(files) == 0:
            print("✅ Thư mục doctype đã sạch")
        else:
            print("⚠️  Thư mục doctype vẫn có files")
    else:
        print("❌ Thư mục doctype không tồn tại")

if __name__ == "__main__":
    check_reset_status()

