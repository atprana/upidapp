import frappe

@frappe.whitelist()
def get_default_warehouse(itemcode):	
	return frappe.db.sql("""select default_warehouse from `tabItem Default` itdef where itdef.parent = %s limit 1""",itemcode )	
	
@frappe.whitelist()
def get_employee(userid):
	data = frappe.db.sql("""select name from tabEmployee emp where  emp.user_id = %s""", userid)
	if data is None:
		return ''
	else:
		return data	
	
