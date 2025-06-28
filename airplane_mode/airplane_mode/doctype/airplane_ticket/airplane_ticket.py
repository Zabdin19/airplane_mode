# Copyright (c) 2025, Zain (Xeverse Planet) and contributors
# For license information, please see license.txt

from frappe.website.website_generator import WebsiteGenerator
import frappe
import random
from frappe.model.document import Document 


class AirplaneTicket(Document):
    def before_insert(self):
        row_number = random.randint(1, 99)
        seat_letter = random.choice(['A', 'B', 'C', 'D', 'E'])
        self.seat = f"{row_number}{seat_letter}"

    def before_save(self):
        total_add_ons = sum(addon.amount for addon in self.add_ons if addon.amount)
        self.total_amount = (self.flight_price or 0) + total_add_ons

    def validate(self):
        self.remove_duplicate_add_ons()
        self.check_seat_capacity()

    def remove_duplicate_add_ons(self):
        unique_addons = {}
        cleaned_addons = []
        for addon in self.add_ons:
            if addon.item not in unique_addons:
                unique_addons[addon.item] = True
                cleaned_addons.append(addon)
        self.add_ons = cleaned_addons

    def check_seat_capacity(self):
        if not self.airplane_flight:
            return

        # Step 1: Get the flight document
        flight = frappe.get_doc("Airplane Flight", self.airplane_flight)

        # Step 2: Get the airplane from the flight
        airplane = frappe.get_doc("Airplane", flight.airplane)

        # Step 3: Count tickets for this flight
        ticket_count = frappe.db.count("Airplane Ticket", {
            "airplane_flight": self.airplane_flight,
            "docstatus": ["<", 2]  # Include draft & submitted, exclude cancelled
        })

        # Step 4: Throw error if capacity exceeded
        if ticket_count >= airplane.capacity:
            frappe.throw(f"Cannot create ticket. All {airplane.capacity} seats are already booked for this flight.")

    def before_submit(self):
        if not self.gate_number:
            frappe.throw("Gate Number is required before submitting the ticket.")

        if self.status != "Boarded":
            frappe.throw("You can only submit the ticket if the passenger is Boarded.")
            
    def after_submit(self):
        self.status = "Completed"
        self.db_set("status", "Completed")
