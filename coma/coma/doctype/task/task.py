# Copyright (c) 2025, Vu Linh and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from coma.services.progress_calculator import (
    calculate_task_progress,
    update_category_progress,
    update_project_progress
)


class Task(Document):
    def on_update(self):
        """
        Hook: Khi task được update.
        
        Logic:
        1. Nếu status thay đổi → Tính lại task progress
        2. Update category progress
        3. Update project progress
        """
        if self.has_value_changed('status'):
            # Update task progress
            self.progress_percentage = calculate_task_progress(self)
            self.db_update()
            
            # Update category progress
            if self.category:
                category = frappe.get_doc('Category', self.category)
                update_category_progress(category)
                category.db_update()
                
                # Update project progress
                if category.project:
                    project = frappe.get_doc('Project', category.project)
                    update_project_progress(project)
                    project.db_update()
            
            # Commit changes
            frappe.db.commit()
