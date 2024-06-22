// Copyright (c) 2024, osama and contributors
// For license information, please see license.txt

 frappe.ui.form.on("Ride Booking", {
 	refresh(frm) {




	},
    rate(frm){
        frm.trigger("update_total_amount");

        //recalculate total

    },
    update_total_amount(frm){

        let total_d =0;
        for(let Item of frm.doc.items){
            total_d += Item.distance;
    }
    const amount = frm.doc.rate * total_d;
    frm.set_value("Total amount",amount)
    }
    
    
 });
 frappe.ui.form.on('Ride Booking Item', {
	refresh(frm) {
		// your code here
	},
    distance(frm, cdt,cdn){
        frm.trigger("update_total_amount");
      
},
items_remove(frm){
    frm.trigger("update_total_amount");


}

}
)
