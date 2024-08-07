// Copyright (c) 2024, osama and contributors
// For license information, please see license.txt

frappe.query_reports["Ride Order Script"] = {
    "filters": [
        {
            "fieldname": "customer_name",
            "label": ("Customer Name"),
            "fieldtype": "Data",
            "default": ""
        },
        {
            "fieldname": "contact_number",
            "label": ("Contact Number"),
            "fieldtype": "Data",
            "default": ""
        },
        {
            "fieldname": "status",
            "label": ("Status"),
            "fieldtype": "Select",
            "options": ["New", "Accepted", "Rejected"],
            "default": ""
        },
        {
            "fieldname": "ride_count",
            "label": ("Ride Count"),
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
                doctype: "Ride Order",
                fields: ["customer_name", "contact_number", "status", "ride_count"],
                filters: filters
            },
            callback: function(response) {
                const data = response.message;

                // Create Chart
                let statusCounts = {};
                data.forEach(order => {
                    if (!statusCounts[order.status]) {
                        statusCounts[order.status] = 0;
                    }
                    statusCounts[order.status]++;
                });

                let labels = Object.keys(statusCounts);
                let values = Object.values(statusCounts);

                new frappe.Chart("#chart", {
                    data: {
                        labels: labels,
                        datasets: [
                            {
                                name: "Orders by Status",
                                values: values
                            }
                        ]
                    },
                    type: 'pie', // or 'bar', 'line', etc.
                    height: 300
                });
            }
        });
    }
}
