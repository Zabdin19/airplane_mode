# Copyright (c) 2025, Zain (Xeverse Planet) and contributors
# For license information, please see license.txt

import frappe
from frappe.query_builder import DocType
from pypika import functions as fn

def execute(filters=None):
    columns = [
        {"label": "Airline", "fieldname": "airline", "fieldtype": "Link", "options": "Airline", "width": 200},
        {"label": "Revenue", "fieldname": "revenue", "fieldtype": "Currency", "width": 150},
    ]

    # Define DocTypes
    Ticket = DocType("Airplane Ticket")
    Flight = DocType("Airplane Flight")

    # Get all Airlines
    airlines = frappe.get_all("Airline", fields=["name"])

    # Get revenue grouped by airline using join
    revenue_data = (
        frappe.qb
        .from_(Ticket)
        .join(Flight)
        .on(Ticket.flight == Flight.name)
        .select(Flight.airline, fn.Sum(Ticket.total_amount).as_("revenue"))
        .groupby(Flight.airline)
    ).run(as_dict=True)

    # Map results
    revenue_map = {row["airline"]: row["revenue"] or 0 for row in revenue_data}

    # Final rows with 0-revenue airlines included
    data = []
    total_revenue = 0
    for airline in airlines:
        revenue = revenue_map.get(airline.name, 0)
        total_revenue += revenue
        data.append({
            "airline": airline.name,
            "revenue": revenue
        })

    # Report Summary
    report_summary = [
        {
            "label": "Total Revenue",
            "value": total_revenue,
            "indicator": "green"
        }
    ]

    # Donut Chart
    chart = {
        "data": {
            "labels": [row["airline"] for row in data],
            "datasets": [{"name": "Revenue", "values": [row["revenue"] for row in data]}]
        },
        "type": "donut"
    }

    return columns, data, None, chart, report_summary
