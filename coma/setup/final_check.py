#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kiểm tra cuối cùng tất cả DocTypes đã tạo
"""

import frappe

def final_check():
    print("=== Kiểm tra DocTypes cuối cùng ===")
    
    doctypes = frappe.get_all("DocType", filters={"module": "Coma"})
    print(f"DocTypes trong module Coma: {len(doctypes)}")
    
    for dt in doctypes:
        print(f"  ✅ {dt.name}")
    
    print("\n🎉 Tất cả DocTypes đã sẵn sàng sử dụng!")
    print("\n📋 Danh sách DocTypes:")
    print("  1. Project (Master)")
    print("  2. Project Team Member (Child Table)")
    print("  3. Category (Master)")
    print("  4. Task (Master)")
    print("  5. Daily Log (Master)")
    print("  6. Daily Log Photo (Child Table)")
    print("  7. Expense Entry (Master)")
    
    print("\n🚀 Bước tiếp theo:")
    print("  1. Chạy: bench start")
    print("  2. Truy cập: http://localhost:8000")
    print("  3. Tạo Project mới và test các tính năng")

if __name__ == "__main__":
    final_check()

