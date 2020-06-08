import frappe

def beforeSubmit(doc, method):
    if method == 'before_submit':
        if doc.owner == frappe.session.user and not 'Self Submitter' in frappe.get_roles(frappe.session.user):
            frappe.throw("Submitting your own documents is not permitted")


def beforeInsertAll(doc, method):
	try:
		doc.input_by = frappe.session.user
	except Exception as e:
		pass
	
def beforeSubmitAll(doc, method):
	try:
		doc.submit_by = frappe.session.user

	except Exception as e:
		pass 