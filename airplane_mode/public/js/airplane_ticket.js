frappe.ui.form.on('Airplane Ticket', {
    refresh: function(frm) {
        // "Assign Seat" option inside "Action" dropdown button
        frm.add_custom_button(__('Assign Seat'), () => {
            frappe.prompt([
                {
                    label: 'Seat Number',
                    fieldname: 'seat_number',
                    fieldtype: 'Data',
                    reqd: true
                }
            ],
            function(values) {
                frm.set_value('seat', values.seat_number);
                frappe.msgprint(`Seat <b>${values.seat_number}</b> assigned.`);
            },
            'Assign Seat');
        }, __('Action'));  // This makes "Assign Seat" a dropdown item under "Action"
    }
});
