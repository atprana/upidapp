# Copyright (c) 2013, atprana and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
# import frappe
from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import flt

def execute(filters=None):
	if not filters: filters = {}

	columns = get_columns()
	data = get_supplier(filters)

	return columns, data

def get_columns():
	return [
		_("Supplier Name") + ":Data:120" 		
	]

def get_supplier(filters):
	conditions = get_conditions(filters)
	return frappe.db.sql("""select suplier_name from tabSupplier """ , as_list=1)

pi