// Copyright (c) 2024, osama and contributors
// For license information, please see license.txt

frappe.query_reports["Ride Booking Script"] = {
    "filters": [
        {
            "fieldname": "order",
            "label": ("Order"),
            "fieldtype": "Link",
            "options": "Ride Booking",
            "default": ""
        },
        {
            "fieldname": "drivers",
            "label": ("Drivers"),
            "fieldtype": "Link",
            "options": "Drivers",
            "default": ""
        },
        {
            "fieldname": "still_editable",
            "label": ("Still Editable"),
            "fieldtype": "Check",
            "default": ""
        },
        {
            "fieldname": "amended_from",
            "label": ("Amended From"),
            "fieldtype": "Link",
            "options": "Ride Booking",
            "default": ""
        },
        {
            "fieldname": "vehicle",
            "label": ("Vehicle"),
            "fieldtype": "Link",
            "options": "Vehicles",
            "default": ""
        },
        {
            "fieldname": "rate",
            "label": ("Rate"),
            "fieldtype": "Currency",
            "default": ""
        },
        {
            "fieldname": "total_amount",
            "label": ("Total Amount"),
            "fieldtype": "Currency",
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
                doctype: "Ride Booking",
                fields: ["order", "drivers", "still_editable", "amended_from", "vehicle", "rate", "total_amount"],
                filters: filters
            },
            callback: function(response) {
                const data = response.message;

                // Create Chart
                let totalAmounts = {};
                data.forEach(booking => {
                    let vehicle = booking.vehicle;
                    let amount = booking.total_amount;
                    if (!totalAmounts[vehicle]) {
                        totalAmounts[vehicle] = 0;
                    }
                    totalAmounts[vehicle] += amount;
                });

                let labels = Object.keys(totalAmounts);
                let values = Object.values(totalAmounts);

                new frappe.Chart("#chart", {
                    data: {
                        labels: labels,
                        datasets: [
                            {
                                name: "Total Amount by Vehicle",
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

