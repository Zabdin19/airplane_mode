# Copyright (c) 2025, Zain (Xeverse Planet) and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import flt

def execute(filters=None):
    columns = [
        {"label": "Airport", "fieldname": "airport", "fieldtype": "Link", "options": "Airport", "width": 200},
        {"label": "Total Shops", "fieldname": "total_shops", "fieldtype": "Int", "width": 120},
        {"label": "Occupied Shops", "fieldname": "occupied_shops", "fieldtype": "Int", "width": 140},
        {"label": "Available Shops", "fieldname": "available_shops", "fieldtype": "Int", "width": 140},
    ]

    data = frappe.db.sql("""
        SELECT
            airport,
            COUNT(name) AS total_shops,
            SUM(CASE WHEN is_occupied = 1 THEN 1 ELSE 0 END) AS occupied_shops,
            SUM(CASE WHEN is_occupied = 0 THEN 1 ELSE 0 END) AS available_shops
        FROM `tabShop`
        GROUP BY airport
    """, as_dict=True)

    return columns, data
