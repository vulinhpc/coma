#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Check DocTypes in COMA app
"""

import frappe

def check_doctypes():
    print("=== Kiểm tra DocTypes trong database ===")
    print("DocTypes trong module COMA:")
    result = frappe.db.sql("SELECT name FROM `tabDocType` WHERE module='COMA'")
    print(result)

    print("\n=== Kiểm tra bằng get_all ===")
    doctypes = frappe.get_all("DocType", filters={"module": "COMA"})
    print(doctypes)

    print("\n=== Kiểm tra apps đã install ===")
    apps = frappe.get_installed_apps()
    print("Installed apps:", apps)

    print("\n=== Kiểm tra chi tiết từng DocType ===")
    for doctype in doctypes:
        name = doctype.name
        print(f"\n--- {name} ---")
        try:
            meta = frappe.get_meta(name)
            print(f"Module: {meta.module}")
            print(f"Is Table: {meta.istable}")
            print(f"Is Submittable: {meta.is_submittable}")
            print(f"Fields count: {len(meta.fields)}")
        except Exception as e:
            print(f"Error getting meta for {name}: {e}")

    print("\n=== Kiểm tra hoàn tất ===")

if __name__ == "__main__":
    check_doctypes()

