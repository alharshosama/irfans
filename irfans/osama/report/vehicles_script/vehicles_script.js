// Copyright (c) 2024, osama and contributors
// For license information, please see license.txt

frappe.query_reports["Vehicles Script"] = {
    "filters": [
        {
            "fieldname": "title",
            "label": ("Title"),
            "fieldtype": "Data",
            "default": ""
        },
        {
            "fieldname": "model",
            "label": ("Model"),
            "fieldtype": "Data",
            "default": ""
        },
        {
            "fieldname": "make",
            "label": __("Make"),
            "fieldtype": "Data",
            "default": ""
        },
        {
            "fieldname": "year",
            "label": ("Year"),
            "fieldtype": "Int",
            "default": ""
        },
        {
            "fieldname": "color",
            "label": ("Color"),
            "fieldtype": "Data",
            "default": ""
        },
        {
            "fieldname": "route",
            "label": ("Route"),
            "fieldtype": "Data",
            "default": ""
        },
        {
            "fieldname": "status",
            "label": ("Status"),
            "fieldtype": "Select",
            "options": ["Active", "Out of Service", "Sold", "Crushed"],
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
                doctype: "Vehicles",
                fields: ["title", "model", "make", "year", "color", "route", "status"],
                filters: filters
            },
            callback: function(response) {
                const data = response.message;

                // Create Chart
                let statusCounts = {};
                data.forEach(vehicle => {
                    let status = vehicle.status;
                    if (!statusCounts[status]) {
                        statusCounts[status] = 0;
                    }
                    statusCounts[status]++;
                });

                let labels = Object.keys(statusCounts);
                let values = Object.values(statusCounts);

                new frappe.Chart("#chart", {
                    data: {
                        labels: labels,
                        datasets: [
                            {
                                name: "Vehicles by Status",
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
