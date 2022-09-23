# Copyright (c) 2013, atprana and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
import barcode  
from barcode.writer import ImageWriter

def execute(filters=None):
	columns, data, item_list = [], [], []
	Code39 = barcode.get_barcode_class('ean13')



	columns = [
		{"label": _("Item Code"), "fieldname": "item_code", "fieldtype": "Link", "options": "Item", "width": 140},
		{"label": _("Item Name"), "fieldname": "item_name", "width": 100},
		{"label": "Barcode", "fieldname": "barcode", "fieldtype": "Image"}
		];

	data = frappe.db.sql("""select item_code, item_name, %(bc)s  as barcode 
			from tabItem order by item_code""", { "bc" : Code39('1234543000000', writer=ImageWriter())})


	return columns, data

# EAN = barcode.get_barcode_class('ean13')
# ean = EAN(u'123456789011', writer=ImageWriter())
# fullname = ean.save('my_ean13_barcode')