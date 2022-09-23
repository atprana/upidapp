// Copyright (c) 2016, atprana and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Test Script"] = {
	"filters": [
		{
			"fieldname": "item_code",
			"label": __("Item Code"),
			"fieldtype": "Link",
			"options": "Item"
		},
		{
			"fieldname": "from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
		},
		{
			"fieldname": "to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
		}




	]
};
