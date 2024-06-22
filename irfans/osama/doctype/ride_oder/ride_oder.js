// Copyright (c) 2024, osama and contributors
// For license information, please see license.txt

frappe.ui.form.on("Ride Order", {
    onload(frm) {
        // Triggered when the form is loaded
        console.log("Form loaded...");
    },
    setup(frm) {
        // Triggered when the form is set up
        console.log("Form setup...");
    },
    refresh(frm) {
        // Triggered when the form is refreshed
        console.log("Form refreshed...");

        // Check if the status is "New"
        if (frm.doc.status == "New") {
            // Add a custom button labeled "Accept"
            frm.add_custom_button("Accept", () => {
                console.log("Accept button clicked");
                // Set the status field to "Accepted"
                frm.set_value("status", "Accepted");
                
                // Save the form
                frm.save().then(() => {
                    console.log("Form saved with status Accepted");
                }).catch((error) => {
                    console.error("Error saving form:", error);
                });
            }, "Actions");

            // Add a custom button labeled "Reject"
            frm.add_custom_button("Reject", () => {
                console.log("Reject button clicked");
                // Set the status field to "Rejected"
                frm.set_value("status", "Rejected");
                
                // Save the form
                frm.save().then(() => {
                    console.log("Form saved with status Rejected");
                }).catch((error) => {
                    console.error("Error saving form:", error);
                });
            }, "Actions");
        }
    },
    status(frm) {
        // Triggered when the status field is changed
        console.log("Status changed to:", frm.doc.status);
    }
});
