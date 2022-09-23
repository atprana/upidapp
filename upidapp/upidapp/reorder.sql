select item.item_code, item.item_name
-- , b.warehouse, b.actual_qty, b.projected_qty
      -- , ir.warehouse_reorder_level, ir.warehouse_reorder_qty 
      from `tabItem` item 
		-- join tabBin b on item.item_code = b.item_code
		 -- join `tabItem Reorder` ir on (item.item_code = ir.parent and b.warehouse = ir.warehouse)
		where is_stock_item=1 and has_variants=0
			and disabled=0
			and (end_of_life is null or end_of_life='0000-00-00' or end_of_life > curdate())
			and (exists (select name from `tabItem Reorder` ir where ir.parent=item.name)
				or (variant_of is not null and variant_of != ''
				and exists (select name from `tabItem Reorder` ir where ir.parent=item.variant_of))
			) order by item_code