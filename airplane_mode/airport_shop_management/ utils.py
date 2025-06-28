import frappe

def send_rent_reminders():
    if not frappe.db.get_single_value("Shop Settings", "enable_rent_reminders"):
        return

    contracts = frappe.get_all("Shop Lease Contract", fields=["tenant", "monthly_rent", "expiry_date"], filters={"status": "Active"})

    for contract in contracts:
        tenant = frappe.get_doc("Tenant", contract.tenant)
        if tenant.email:
            frappe.sendmail(
                recipients=[tenant.email],
                subject="Monthly Rent Reminder",
                message=f"Dear {tenant.name},<br>Your monthly rent of Rs. {contract.monthly_rent} is due. Kindly make the payment.<br><br>Thanks,<br>Airport Management"
            )
