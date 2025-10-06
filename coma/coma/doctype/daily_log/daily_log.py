# Copyright (c) 2025, Vu Linh and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class DailyLog(Document):
    def autoname(self):
        if not self.name:
            self.name = f"LOG-{frappe.utils.now_datetime().strftime('%Y%m%d%H%M%S')}"

