from time import strptime
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
	last_date = datetime.strptime(last_date, '%Y-%m-%d').date() if isinstance(last_date,str) else last_date

	if is_locked:
		if hasattr(doc,"transaction_date") and doc.transaction_date is not None:
			transaction_date = datetime.strptime(doc.transaction_date, '%Y-%m-%d').date() if isinstance(doc.transaction_date, str) else doc.transaction_date 
			if  transaction_date  < last_date:
					frappe.msgprint( ("Transaction Date before {0} already locked").format(last_date))
					raise frappe.ValidationError
		if hasattr(doc,"posting_date") and doc.posting_date is not None:
			posting_date = datetime.strptime(doc.posting_date, '%Y-%m-%d').date() if isinstance(doc.posting_date, str)  else doc.posting_date 
			if posting_date < last_date:	
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
