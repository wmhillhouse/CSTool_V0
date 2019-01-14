
// Filters a table given:
//  - startRow -> Row number to start filtering on (avoid headings, etc.)
//  - input ->
//  - table -> table to filter
//  -
function filter(startRow) {
  // Declare variables
  var startRow, input, filter, table, tr, td, i;
  input = document.getElementById("tag");
  filter = input.value.toUpperCase();
  table = document.getElementById("dataTable");
  tr = table.getElementsByTagName("tr");

  // Loop through all table rows, and hide those who don't match the search query
  for (i = startRow; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[0];
    if (td) {
      if (td.innerHTML.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }
  }
}