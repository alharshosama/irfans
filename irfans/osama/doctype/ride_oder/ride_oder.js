// Copyright (c) 2024, osama and contributors
// For license information, please see license.txt

frappe.ui.form.on("Ride Order", {
    onload(frm) {
        // Triggered when the form is loaded
        console.log("running load...");
    },
    setup(frm) {
        // Triggered when the form is set up
        console.log("setup...");
    },
    refresh(frm) {
        // Triggered when the form is refreshed
        console.log("on refresh....");

        // Check if the status is not "Accepted"
        if (frm.doc.status !== "Accepted") {
            // Add a custom button labeled "Accept"
            frm.add_custom_button("Accept", () => {
                // Show a Frappe alert (commented out)
                // frappe.show_alert("It works!")

                // Set the status field to "Accepted"
                frm.set_value("status", "Accepted");
                
                // Save the form
                frm.save();
            });
        }
    },
});