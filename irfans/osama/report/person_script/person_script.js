// Copyright (c) 2024, osama and contributors
// For license information, please see license.txt

frappe.query_reports["Person Script"] = {
    "filters": [
        {
            "fieldname": "first_name",
            "label": ("First Name"),
            "fieldtype": "Data",
            "default": ""
        },
        {
            "fieldname": "last_name",
            "label": ("Last Name"),
            "fieldtype": "Data",
            "default": ""
        },
        {
            "fieldname": "phone_number",
            "label": ("Phone Number"),
            "fieldtype": "Data",
            "default": ""
        },
        {
            "fieldname": "full_name",
            "label": ("Full Name"),
            "fieldtype": "Data",
            "default": ""
        },
        {
            "fieldname": "age",
            "label": ("Age"),
            "fieldtype": "Int",
            "default": ""
        }
    ],

    "onload": function(report) {
        report.page.add_inner_button(__("Refresh Chart"), function() {
            report.refresh();
        });

        report.refresh();
    },

    "refresh": function(report) {
        let filters = report.get_values();
        frappe.call({
            method: "frappe.client.get_list",
            args: {
                doctype: "Person",
                fields: ["first_name", "last_name", "phone_number", "full_name", "age"],
                filters: filters
            },
            callback: function(response) {
                const data = response.message;

                // Create Chart
                let ageGroups = {};
                data.forEach(person => {
                    if (!ageGroups[person.age]) {
                        ageGroups[person.age] = 0;
                    }
                    ageGroups[person.age]++;
                });

                let labels = Object.keys(ageGroups);
                let values = Object.values(ageGroups);

                let chart = new frappe.Chart("#chart", {
                    data: {
                        labels: labels,
                        datasets: [
                            {
                                name: "Person by Age",
                                values: values
                            }
                        ]
                    },
                    type: 'bar', // or 'line', 'pie', etc.
                    height: 300
                });
            }
        });
    }
}
