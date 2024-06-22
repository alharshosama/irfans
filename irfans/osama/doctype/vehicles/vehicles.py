# Copyright (c) 2024, osama and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator

class Vehicles(WebsiteGenerator):
    def before_save(self):
         self.set_title()
        # self.title = f"{self.make} {self.model}, {self.year}"
		

    def set_title(self):
        self.title = f"{self.make} {self.model},{self.year}"

    def validate(self):
        if self.year <= 2000:
            frappe.throw("Cars year must be at least 2000")

    # def after_insert(self):
    #     frappe.sendmail(recipients=[self.email], message="Thank you for registering!")