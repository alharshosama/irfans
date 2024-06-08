# Copyright (c) 2024, osama and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class Vehicles(Document):
    def before_save(self):
         self.set_title()
        # self.title = f"{self.make} {self.model}, {self.year}"
		

    def set_title(self):
        self.title = f"{self.make} {self.model},{self.year}"