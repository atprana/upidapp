frappe.ui.form.on('Material Request',  {
    onload: function(frm) {
        if (cur_frm.doc.__islocal) {
            frappe.call("upidapp.unipres_util.get_employee", {userid: frappe.session.user})
            .then(r => {
                cur_frm.set_value("request_by", r.message[0][0],"");
            });
        }
    },
    refresh: function(frm) {
        
        // use the __islocal value of doc,  to check if the doc is saved or not
        frm.set_df_property('mr_type',  'read_only',  frm.doc.__islocal ? 0 : 1);
        frm.set_df_property('item_type',  'read_only',  frm.doc.__islocal ? 0 : 1);
        },
 //   item_type: function(frm) {
 //      if (cur_frm.doc.items.length > 1) 
 //      frappe.throw("Can not change type");
 //    }        ,
 	before_insert: function(frm) {
        dep = '';
        frappe.call({ 
            method: "frappe.client.get_value", async:false, 
            args:{ doctype:'Employee', filters:{ user_id: frappe.session.user }, fieldname:['department'] }, 
            callback:function (r)
            { if(r.message !== undefined)
            { dep=r.message.department } } });
            frm.doc.remarks = dep;    
         
        if (frm.doc.material_request_type == "Material Issue" &&  dep !== frm.doc.department) {
            frappe.throw("Can not create request for other department");
        }
	}
});
  
 var l,r=0;
 cur_frm.cscript.onload = function(frm) {
    cur_frm.set_query("item_code", "items", function() {
        var res= {}, grps=[];
        frappe.call({ 
            method: "frappe.client.get_value", async:false, 
            args:{ doctype:'Item Group', filters:{ "item_group_name": cur_frm.doc.item_type}, fieldname:['lft','rgt'] },
        
            callback:function (m)
            {
            if(m.message !== undefined) {
                l=m.message.lft;
                r=m.message.rgt; 
                }
            } 
        });
        frappe.call({ 
            method: "frappe.client.get_list", async:false, 
            // change from > to >= and < to <=
              args:{ doctype:'Item Group', filters: [["lft",">=",l],["rgt","<=",r]],  fieldname:['item_group_name'] }, 
          callback:function (m) { 
                if(m.message !== undefined) 
                    res = m.message;
                    for (let i=0 ; i < res.length; i++ ) { grps.push(res[i].name)}
            }
            
        });
        return  {
            filters:[["item_group", "IN", grps ]]
        };
    });
};

