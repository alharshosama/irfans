# Copyright (c) 2024, osama and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

# Controller class
class Person(Document):
    def before_save(self):
        self.full_name = f"{self.first_name} {self.last_name}"
    
    def send_alert(self):
        print("sending Message")

    def validate(self):
        if self.age <= 18:
            frappe.throw("Person's age must be at least 18")

    def after_insert(self):
        frappe.sendmail(recipients=[self.email], message="Thank you for registering!")
	# def save(self, "Person"):
    #     super().save("Person") # call the base save method
    #     do_something()