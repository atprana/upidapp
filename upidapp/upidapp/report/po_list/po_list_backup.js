frappe.query_reports["PO List"] = {
  "filters": [],

  "formatter": function (value, row, column, data, default_formatter) {
    value = default_formatter(value, row, column, data);

    if (column.id == "INVOICE STATUS") {
      status = data["INVOICE STATUS"]
      if (data["INVOICE STATUS"] == "Paid") {
        value = "<span style='font-weight: bold; color:green; background-color:white'>" + value + "</span>";
      } else
        if (data["INVOICE STATUS"] == "Partially Paid") {
          value = "<span style='font-weight: bold; color:orange; background-color:white'>" + value + "</span>";
        }
        else
          if ((data["INVOICE STATUS"] == "Unpaid" || data["INVOICE STATUS"] == "Overdue") {
            value = "<span style='font-weight: bold; color:red; background-color:white'>" + value + "</span>";
          }
    }
    return value;
  }
}
