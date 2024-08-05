# Copyright (c) 2024, osama and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
    columns, data = [], []

    # Define the columns of the report
    columns = [
        {
            "fieldname": "first_name",
            "label": ("First Name"),
            "fieldtype": "Data",
            "width": 150
        },
        {
            "fieldname": "last_name",
            "label": ("Last Name"),
            "fieldtype": "Data",
            "width": 150
        },
        {
            "fieldname": "phone_number",
            "label": ("Phone Number"),
            "fieldtype": "Data",
            "width": 150
        },
        {
            "fieldname": "full_name",
            "label": ("Full Name"),
            "fieldtype": "Data",
            "width": 200
        },
        {
            "fieldname": "age",
            "label": ("Age"),
            "fieldtype": "Int",
            "width": 100
        }
    ]

    # Fetch data from the 'Person' doctype with filters
    conditions = ""
    if filters.get("first_name"):
        conditions += " AND first_name=%(first_name)s"
    if filters.get("last_name"):
        conditions += " AND last_name=%(last_name)s"
    if filters.get("phone_number"):
        conditions += " AND phone_number=%(phone_number)s"
    if filters.get("full_name"):
        conditions += " AND full_name=%(full_name)s"
    if filters.get("age"):
        conditions += " AND age=%(age)s"
    
    query = f"""
        SELECT 
            first_name, last_name, phone_number, full_name, age
        FROM 
            `tabPerson`
        WHERE 
            1=1
            {conditions}
    """
    
    data = frappe.db.sql(query, filters, as_dict=True)

    # Adding chart
    age_groups = {}
    for row in data:
        age = row['age']
        if age not in age_groups:
            age_groups[age] = 0
        age_groups[age] += 1

    chart = {
        "data": {
            "labels": list(age_groups.keys()),
            "datasets": [
                {
                    "name": "Person by Age",
                    "values": list(age_groups.values())
                }
            ]
        },
        "type": "bar",  # or 'line', 'pie', etc.
        "height": 300
    }

    return columns, data, None, chart