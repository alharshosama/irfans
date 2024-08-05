# Copyright (c) 2024, osama and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
    columns, data = [], []

    # Define the columns of the report
    columns = [
        {
            "fieldname": "title",
            "label": ("Title"),
            "fieldtype": "Data",
            "width": 150
        },
        {
            "fieldname": "model",
            "label": ("Model"),
            "fieldtype": "Data",
            "width": 150
        },
        {
            "fieldname": "make",
            "label": ("Make"),
            "fieldtype": "Data",
            "width": 150
        },
        {
            "fieldname": "year",
            "label": ("Year"),
            "fieldtype": "Int",
            "width": 100
        },
        {
            "fieldname": "color",
            "label": ("Color"),
            "fieldtype": "Data",
            "width": 100
        },
        {
            "fieldname": "route",
            "label": ("Route"),
            "fieldtype": "Data",
            "width": 150
        },
        {
            "fieldname": "status",
            "label": ("Status"),
            "fieldtype": "Select",
            "options": "\nActive\nOut of Service\nSold\nCrushed",
            "width": 150
        }
    ]

    # Fetch data from the 'Vehicles' doctype with filters
    conditions = ""
    if filters.get("title"):
        conditions += " AND title=%(title)s"
    if filters.get("model"):
        conditions += " AND model=%(model)s"
    if filters.get("make"):
        conditions += " AND make=%(make)s"
    if filters.get("year"):
        conditions += " AND year=%(year)s"
    if filters.get("color"):
        conditions += " AND color=%(color)s"
    if filters.get("route"):
        conditions += " AND route=%(route)s"
    if filters.get("status"):
        conditions += " AND status=%(status)s"
    
    query = f"""
        SELECT 
            title, model, make, year, color, route, status
        FROM 
            `tabVehicles`
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
                    "name": "Vehicles by Status",
                    "values": list(status_counts.values())
                }
            ]
        },
        "type": "pie",  # or 'bar', 'line', etc.
        "height": 300
    }

    return columns, data, None, chart