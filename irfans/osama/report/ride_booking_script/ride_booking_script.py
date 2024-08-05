# Copyright (c) 2024, osama and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
    columns, data = [], []

    # Define the columns of the report
    columns = [
        {
            "fieldname": "order",
            "label": ("Order"),
            "fieldtype": "Link",
            "options": "Ride Booking",
            "width": 150
        },
        {
            "fieldname": "drivers",
            "label": ("Drivers"),
            "fieldtype": "Link",
            "options": "Drivers",
            "width": 150
        },
        {
            "fieldname": "still_editable",
            "label": ("Still Editable"),
            "fieldtype": "Check",
            "width": 100
        },
        {
            "fieldname": "amended_from",
            "label": ("Amended From"),
            "fieldtype": "Link",
            "options": "Ride Booking",
            "width": 150
        },
        {
            "fieldname": "vehicle",
            "label": ("Vehicle"),
            "fieldtype": "Link",
            "options": "Vehicles",
            "width": 150
        },
        {
            "fieldname": "rate",
            "label": ("Rate"),
            "fieldtype": "Currency",
            "width": 100
        },
        {
            "fieldname": "total_amount",
            "label": ("Total Amount"),
            "fieldtype": "Currency",
            "width": 100
        }
    ]

    # Fetch data from the 'Ride Booking' doctype with filters
    conditions = ""
    if filters.get("order"):
        conditions += " AND order=%(order)s"
    if filters.get("drivers"):
        conditions += " AND drivers=%(drivers)s"
    if filters.get("still_editable") is not None:
        conditions += " AND still_editable=%(still_editable)s"
    if filters.get("amended_from"):
        conditions += " AND amended_from=%(amended_from)s"
    if filters.get("vehicle"):
        conditions += " AND vehicle=%(vehicle)s"
    if filters.get("rate"):
        conditions += " AND rate=%(rate)s"
    if filters.get("total_amount"):
        conditions += " AND total_amount=%(total_amount)s"
    
    query = f"""
        SELECT 
            `order`, drivers, still_editable, amended_from, vehicle, rate, total_amount
        FROM 
            `tabRide Booking`
        WHERE 
            1=1
            {conditions}
    """
    
    data = frappe.db.sql(query, filters, as_dict=True)

    # Generate chart data
    total_amounts = {}
    for row in data:
        vehicle = row['vehicle']
        total_amount = row['total_amount']
        if vehicle not in total_amounts:
            total_amounts[vehicle] = 0
        total_amounts[vehicle] += total_amount

    chart = {
        "data": {
            "labels": list(total_amounts.keys()),
            "datasets": [
                {
                    "name": "Total Amount by Vehicle",
                    "values": list(total_amounts.values())
                }
            ]
        },
        "type": "bar",  # or 'line', 'pie', etc.
        "height": 300
    }

    return columns, data, None, chart