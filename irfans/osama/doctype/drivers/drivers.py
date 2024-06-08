# Copyright (c) 2024, osama and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Drivers(Document):
	def before_save(self):
		self.full_name = f"{self.first_name} {self.last_name}"
	pass	


	def send_alert(self):
		print("sending Message")	
       





# API Secret: df6d3d8dd034ba6 