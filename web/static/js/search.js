function search() {
    var input, filter, table, text, tr, td;
    
    input = document.getElementById("bot-search");
    filter = input.value.toUpperCase();
    table = document.getElementById("bot-table");
    tr = table.getElementsByTagName("tr");

    for (var i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[1];
        if (td) {
            text = td.textContent || td.innerText;
            if (text.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
    }
}