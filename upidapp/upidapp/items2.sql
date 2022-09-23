select i.item_code, a.warehouse as warehouse, i.stock_uom as UOM, actual_qty, requested_qty, ordered_qty, projected_qty, reorder_level, reorder_level - projected_qty as shortage_qty
 from `tabItem` i
JOIN 

( -- combine bin and ItemReorder to include all active item in bin also item that
  -- have reorder level set but not active (not in the bin table)

select b.item_code as item_code , b.warehouse, actual_qty, indented_qty as requested_qty, ordered_qty, projected_qty, if(warehouse_reorder_level is NULL,0, warehouse_reorder_level)  as reorder_level from `tabBin` b 
		left join `tabItem Reorder` ir  on item_code = ir.parent and b.warehouse= ir.warehouse
UNION
select ir.parent as item_code, ir.warehouse as warehouse, 0 as actual_qty,0 as requested_qty, 0 as ordered_qty, 0 as projected_qty, warehouse_reorder_level as reorder_level from `tabItem Reorder` ir where not exists(select item_code from tabBin where tabBin.item_code = ir.parent and tabBin.warehouse=ir.warehouse) 
) a

-- join with filtered tabItem  
on a.item_code=i.item_code 

where i.is_stock_item=1 
	and (has_variants=0 )
	and disabled=0
	and (end_of_life is null or end_of_life='0000-00-00' or end_of_life > curdate())
	and reorder_level >= projected_qty

order by i.item_code