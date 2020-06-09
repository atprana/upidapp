# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
			{
			"label": _("Reports"),
			"icon": "fa fa-print",
			"items": [
				{
					"type": "report",
					"name": "Stock Ledger Custom",
					"doctype": "Stock Ledger Entry",
					"is_query_report": True
				},
				{
					"type": "report",
					"name": "Purchase Order List",
					"doctype": "Purchase Order",
					"is_query_report": True
				},
				
			]
		},
	]
