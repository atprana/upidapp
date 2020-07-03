import frappe

def beforeInsertAll(doc, method):
	try:
		doc.input_by = frappe.session.user
		doc.submit_by = ""
	
	except Exception as e: 
		pass		# ignore if doctype dont have attributes input_by, submit_by
	
def beforeSubmitAll(doc, method):
	try:
		doc.submit_by = frappe.session.user	
		if ((doc.input_by == doc.submit_by) and 'Self Submitter' not in frappe.get_roles()):
			frappe.throw("Input and Submit person should be different")
	
	except Exception as e:
		pass	

def projectedQtyChange(doc,method):
	frappe.db.set_value('Item', doc.item_code, 'total_projected_qty', doc.projected_qty)