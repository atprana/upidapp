# Copyright (c) 2013, atprana and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
from frappe import _
import frappe
from frappe.utils import flt, nowdate, add_days, cint

import datetime

def execute(filters=None):
	columns, data = [], []
	columns = [
		{"label": _("Item"), "fieldname": "item_code", "fieldtype": "Link", "options": "Item", "width": 130},
		{"label": _("Item Name"), "fieldname": "item_name", "fieldtype": "Data", "width": 300},
		{"label":_("Warehouse"), "fieldname": "warehouse", "fieldtype": "Link", "options": "Warehouse", "width": 100},
		{"label": _("Actual Qty"), "fieldname": "actual_qty", "fieldtype": "Data", "width": 130},
		{"label": _("Projected Qty"), "fieldname": "projected_qty", "fieldtype": "Data", "width": 130},
	
		]
	# items = item_to_order()
	
	data=item_to_order()


	return columns, data

def item_to_order():
	item_order_data=[]
	item_query = """select item.item_code, item.item_name , b.warehouse,  b.projected_qty from `tabItem` item 
		join tabBin b on item.item_code = b.item_code
		where is_stock_item=1 and has_variants
			and disabled=0
			and (end_of_life is null or end_of_life='0000-00-00' or end_of_life > %(today)s)
			and (exists (select name from `tabItem Reorder` ir where ir.parent=item.name)
				or (variant_of is not null and variant_of != ''
				and exists (select name from `tabItem Reorder` ir where ir.parent=item.variant_of))
			)"""
	items_to_consider = frappe.db.sql( item_query, {"today": nowdate()}, as_dict = True)	

	if not items_to_consider:
		return

	for d in items_to_consider:
		rec = {
			"item_code": d.item_code,
			"item_name": d.item_name,
			"warehouse": d.warehouse,
			# "actual_qty": d.actual_qty,
			"projected_qty": d.projected_qty
		}
		item_order_data.append(rec)

	return item_order_data	