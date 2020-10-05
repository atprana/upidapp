import frappe
from datetime import *

def beforeInsertAll(doc, method):
	if hasattr(doc,"input_by"):	
		doc.input_by = frappe.session.user
	if hasattr(doc,"submit_by"):		
		doc.submit_by = ""
		


def beforeSubmitAll(doc, method):
	last_date = frappe.db.get_single_value("Unipres Transaction Lock Setting", "last_transaction_date")
	is_locked = frappe.db.get_single_value("Unipres Transaction Lock Setting", "enable_lock")

	if is_locked:
		if hasattr(doc,"transaction_date"):
			if  doc.transaction_date < last_date:
				frappe.msgprint( ("Transaction Date before {0} already locked").format(last_date))
				raise frappe.ValidationError
		if hasattr(doc,"posting_date"):
			if  doc.posting_date < last_date:
				frappe.msgprint( ("Posting Date before {0} already locked").format(last_date))
				raise frappe.ValidationError		
	

	if hasattr(doc,"submit_by"):
		doc.submit_by = frappe.session.user
		if hasattr(doc,"input_by"):
			if((doc.input_by == doc.submit_by) and 'Self Submitter' not in frappe.get_roles()):
				frappe.msgprint("Input and Submit person should be different")
				raise frappe.ValidationError
	
    
def projectedQtyChange(doc,method):
	frappe.msgprint("total_projected_qty_alert_sent")
	item_doc=frappe.get_doc('Item', doc.item_code)
	if item_doc:
		item_doc.db_set('total_projected_qty_alert_sent', 0)
		if item_doc.total_projected_qty_alert_sent:
			frappe.msgprint('Alert Sent')
		else:
			frappe.msgprint('Alert Not Sent')	
		item_doc.db_set('total_projected_qty_alert_sent', doc.projected_qty, notify=True)
