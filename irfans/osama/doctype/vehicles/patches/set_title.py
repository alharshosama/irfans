import frappe

def execute():
    Vehicles = frappe.db.get_all("vehicle", pluck="name")
    for v in vehicles:
        vehicle = frappe.get_doc("vehicle",v)
        vehicle.set_title() 
        vehicle.save()

    frappe.db.commit()    