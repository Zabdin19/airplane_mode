import frappe

def update_ticket_gate_numbers(flight_name, gate_number):
    tickets = frappe.get_all("Airplane Ticket", filters={"airplane_flight": flight_name}, pluck="name")

    for ticket in tickets:
        frappe.db.set_value("Airplane Ticket", ticket, "gate_number", gate_number)

    frappe.db.commit()
