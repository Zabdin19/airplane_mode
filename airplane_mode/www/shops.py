import frappe

def get_context(context):
    context.shops = frappe.get_all("Shop", fields=["name", "shop_name", "airport"], filters={"is_occupied": 0})
    return context
