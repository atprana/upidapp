import frappe

def beforeSubmit(doc, method):
    if method == 'before_submit':
        if doc.owner == frappe.session.user and not 'Self Submitter' in frappe.get_roles(frappe.session.user):
            frappe.throw("Submitting your own documents is not permitted")
