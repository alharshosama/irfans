// Copyright (c) 2024, osama and contributors
// For license information, please see license.txt

frappe.ui.form.on("Drivers", {
// 	refresh(frm) {

// 	},

       first_name(frm){
            frm.save()
        },
        age(frm){
            frm.save()
        }
});
