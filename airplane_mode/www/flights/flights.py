import frappe

def get_context(context):
    route = frappe.local.form_dict.name
    flight = frappe.get_doc("Airplane Flight", route)

    if not flight.is_published:
        raise frappe.PermissionError("This flight is not published.")

    context.flight = flight
    return context
