# Copyright (c) 2024, osama and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
    frappe.errprint(filters)  # Print filters for debugging

    columns = [
        {
            "fieldname": "customer_name",
            "label": "Customer Name",
            "fieldtype": "Data"
        },
        {
            "fieldname": "vehicle_ride_order",
            "label": "Vehicle Ride Order",
            "fieldtype": "Currency",
            "options": "AED"
        }
    ]
    
    data = frappe.get_all(
        "Ride Order",
        fields=["SUM(vehicle) AS vehicle_ride_order", "customer_name"],
        filters={"docstatus": 1},
        group_by="customer_name"
    )
    
    chart = {
        "data": {
            "labels": [x['customer_name'] for x in data],
            "datasets": [{"values": [x['vehicle_ride_order'] for x in data]}],
        },
        "type": "pie",
    }
    
    return columns, data, "Here is the report", chart
