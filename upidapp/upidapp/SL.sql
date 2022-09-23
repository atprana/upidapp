SELECT
    concat_ws(" ", sle.posting_date, sle.posting_time) as 'Date',
	tabItem.item_code as 'ItemCode',
	tabItem.item_name as 'ItemName',
	tabItem.item_group as 'ItemGroup', 
	sle.warehouse AS Warehouse, 
	tabItem.stock_uom as UOM, 
	sle.actual_qty AS 'Qty', 
	sle.qty_after_transaction AS `BalanceQtY`, 
	sle.incoming_rate AS `IncomingRate`, 
	sle.valuation_rate AS `ValuationRate`, 
	sle.stock_value AS `BalanceValue`, 
	sle.voucher_type AS `VoucherType`, 
	sle.voucher_no AS `VoucherType`, 
	IF
	( ISNULL( mr1.`name`), mr2.`name`, mr1.name) AS 'Request', 
	IF
	( ISNULL( mr1.department ), mr2.department, mr1.department ) AS 'Department', 
	IF
	( ISNULL( mr1.employee_name ), mr2.employee_name, mr1.employee_name ) AS 'Employee',
	mr1.note as 'Note'
FROM
	`tabStock Ledger Entry` AS sle
	LEFT JOIN
	`tabPurchase Receipt Item`
	ON 
		sle.voucher_detail_no = `tabPurchase Receipt Item`.`name`
	LEFT JOIN
	`tabStock Entry Detail`
	ON 
		sle.voucher_detail_no = `tabStock Entry Detail`.`name`
	LEFT JOIN
	`tabMaterial Request` AS mr1
	ON 
		`tabPurchase Receipt Item`.material_request = mr1.`name`
	LEFT JOIN
	`tabMaterial Request` AS mr2
	ON 
		`tabStock Entry Detail`.material_request = mr2.`name`
	INNER JOIN
	tabItem
	ON 
		sle.item_code = tabItem.item_code