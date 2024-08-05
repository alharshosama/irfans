# Copyright (c) 2024, osama and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
    columns, data = [], []

    # Define the columns of the report
    columns = [
        {
            "fieldname": "customer_name",
            "label": ("Customer Name"),
            "fieldtype": "Data",
            "width": 200
        },
        {
            "fieldname": "contact_number",
            "label": ("Contact Number"),
            "fieldtype": "Data",
            "width": 150
        },
        {
            "fieldname": "status",
            "label": ("Status"),
            "fieldtype": "Select",
            "options": "\nNew\nAccepted\nRejected",
            "width": 100
        },
        {
            "fieldname": "ride_count",
            "label": ("Ride Count"),
            "fieldtype": "Int",
            "width": 100
        }
    ]

    # Fetch data from the 'Ride Order' doctype with filters
    conditions = ""
    if filters.get("customer_name"):
        conditions += " AND customer_name=%(customer_name)s"
    if filters.get("contact_number"):
        conditions += " AND contact_number=%(contact_number)s"
    if filters.get("status"):
        conditions += " AND status=%(status)s"
    if filters.get("ride_count"):
        conditions += " AND ride_count=%(ride_count)s"
    
    query = f"""
        SELECT 
            customer_name, contact_number, status, ride_count
        FROM 
            `tabRide Order`
        WHERE 
            1=1
            {conditions}
    """
    
    data = frappe.db.sql(query, filters, as_dict=True)

    # Generate chart data
    status_counts = {}
    for row in data:
        status = row['status']
        if status not in status_counts:
            status_counts[status] = 0
        status_counts[status] += 1

    chart = {
        "data": {
            "labels": list(status_counts.keys()),
            "datasets": [
                {
                    "name": "Orders by Status",
                    "values": list(status_counts.values())
                }
            ]
        },
        "type": "pie",  # or 'bar', 'line', etc.
        "height": 300
    }

    return columns, data, None, chart