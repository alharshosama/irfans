import frappe
@frappe.override_whitelist(allow_guest=True)
def get_emoji():
    return "🤑"