import frappe
from frappe import _

def get_context(context):
    doc = frappe.get_doc("Airline", context.doc.name)
    

    if doc.website:
        frappe.local.response["type"] = "redirect"
        frappe.local.response["location"] = doc.website
   