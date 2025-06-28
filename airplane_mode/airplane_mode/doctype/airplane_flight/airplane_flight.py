# Copyright (c) 2025, Zain (Xeverse Planet) and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class AirplaneFlight(Document):
    def get_context(self, context):
        print("Airplane Flight Web View is rendering for:", self.name)
        if self.airline:
            context.airline_name = frappe.get_doc("Airline", self.airline).name

    def on_update(self):
        if self.has_value_changed("gate_number"):
            frappe.enqueue("airplane_mode.utils.update_ticket_gate_numbers", flight_name=self.name, gate_number=self.gate_number)


    class website:
        condition_field = "is_published"
