// Copyright (c) 2024, osama and contributors
// For license information, please see license.txt

frappe.ui.form.on("Vehicles", {
	refresh(frm) {

	},
   get_summary(frm){
      frm.get_field("summary").$wrapper.append("<h1>Here is your summary</h1>");
   }
    // is_published(frm){
    //     frm.save()
    //  },
    //  year(frm){
    //     frm.save()
    //  },
    //  make(frm){
    //     frm.save()
    //  },
    //  model(frm){
    //     frm.save()
    //  },
   //   status(frm){
   //      frm.save()
   //   },
   //   condition(frm){
   //      frm.save()
   //   }
});
