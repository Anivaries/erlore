// turn off datatable pagination 
$(document).ready(function () {
    $('#table').dataTable({
      "info": false,
            "searching": false,
            "lengthChange": false,
            "ordering": false,
      "fnDrawCallback": function(oSettings) {
          if (oSettings._iDisplayLength > oSettings.fnRecordsDisplay()) {
              $(oSettings.nTableWrapper).find('.dataTables_paginate').hide();
          } else {
               $(oSettings.nTableWrapper).find('.dataTables_paginate').show();
          }
        }
      })
    });
    
// 5 buttons datatable pagination
$.fn.DataTable.ext.pager.numbers_length = 5;
$.fn.DataTable.ext.pager.full_numbers_no_ellipses = function (e, r) { var a = [], n = $.fn.DataTable.ext.pager.numbers_length, t = Math.floor(n / 2), l = function (e, r) { var a; void 0 === r ? (r = 0, a = e) : (a = r, r = e); for (var n = [], t = r; t < a; t++)n.push(t); return n }; return (a = r <= n ? l(0, r) : e <= t ? l(0, n) : e >= r - 1 - t ? l(r - n, r) : l(e - t, e + t + 1)).DT_el = "span", ["first", "previous", a, "next", "last"] };