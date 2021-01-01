function sortByABC() {
    var table, rows, switching, shouldSwitch;

    switching = true;
    table = document.getElementById("bot-table");

    while (switching) {
        switching = false;
        rows = table.rows;

        for (var i = 1; i < (rows.length - 1); i++) {
            shouldSwitch = false;

            var x = rows[i].getElementsByTagName("td")[0];
            var y = rows[i + 1].getElementsByTagName("td")[0];

            if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
                shouldSwitch = true; break;
            }
        }

        if (shouldSwitch) {
            rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
            switching = true;
        }
    }
}


function sortByStatus() {
    alert("Not Yet Implemented.");
}


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
