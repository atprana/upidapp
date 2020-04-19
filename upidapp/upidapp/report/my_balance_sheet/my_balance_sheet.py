from __future__ import unicode_literals
import frappe
from frappe import msgprint, _

def execute(filters=None):
	columns, data = [], []

	data = get_data()
	columns = get_columns()	
	return columns, data



def get_columns():

	columns = [{
    "fieldname": "supplier_name",
    "label": _("Supplier"),
    "fieldtype": "Data",    
    "width": 200
	},
	{
    "fieldname": "po",
    "label": _("Purchase Order"),
    "fieldtype": "Data",    
    "width": 200
	},
	{
    "fieldname": "item_code",
    "label": _("Item Code"),
    "fieldtype": "Data",    
    "width": 100
	},
	{
    "fieldname": "item_name",
    "label": _("Item Name"),
    "fieldtype": "Data",    
    "width": 200
	},
	{
    "fieldname": "qty",
    "label": _("Qty"),
    "fieldtype": "Data",    
    "width": 80
	},
	{
    "fieldname": "uom",
    "label": _("UOM"),
    "fieldtype": "Data",    
    "width": 80
	},
	{
    "fieldname": "rate",
    "label": _("Rate"),
    "fieldtype": "Data",    
    "width": 80
	},
	{
    "fieldname": "amount",
    "label": _("Amount"),
    "fieldtype": "Data",    
    "width": 100
	},
	{
    "fieldname": "recv_no",
    "label": _("Purchase Receipt"),
    "fieldtype": "Data",    
    "width": 200
	},
	{
    "fieldname": "recv_qty",
    "label": _("Rcvd Qty"),
    "fieldtype": "Data",    
    "width": 80
	},
	
	{
    "fieldname": "recv_uom",
    "label": _("Rcvd UOM"),
    "fieldtype": "Data",    
    "width": 80
	},
	{
    "fieldname": "inv_no",
    "label": _("Invoice"),
    "fieldtype": "Data",    
    "width": 200
	},
	{
    "fieldname": "inv_qty",
    "label": _("Inv Qty"),
    "fieldtype": "Data",    
    "width": 80
	},
	{
    "fieldname": "inv_uom",
    "label": _("Inv UOM"),
    "fieldtype": "Data",    
    "width": 80
	},
	{
    "fieldname": "inv_rate",
    "label": _("Inv Rate"),
    "fieldtype": "Data",    
    "width": 80
	},
	{
    "fieldname": "inv_amount",
    "label": _("Inv Amount"),
    "fieldtype": "Data",    
    "width": 100
	}

	]

	return columns


def get_data():

	data = frappe.db.sql("select * from viewPOStatus", as_dict=1)

	return data
		