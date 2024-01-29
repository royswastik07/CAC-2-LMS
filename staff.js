
var totalReceived = 0;
var totalDelivered = 0;
var totalPending = 0;

function addOrder() {
    var product = document.getElementById("product").value;
    var quantity = document.getElementById("quantity").value;
    var price = document.getElementById("price").value;
    var status = document.getElementById("status").value;

    var table = document.querySelector("table tbody");
    var row = table.insertRow(table.rows.length);

    var cell1 = row.insertCell(0);
    var cell2 = row.insertCell(1);
    var cell3 = row.insertCell(2);
    var cell4 = row.insertCell(3);
    var cell5 = row.insertCell(4);

    cell1.innerHTML = '<input type="checkbox" onchange="updateLiveStatus(this)">';
    cell2.innerHTML = product;
    cell3.innerHTML = quantity;
    cell4.innerHTML = "$" + price;
    cell5.innerHTML = status;

    updateStatusCount(status, 1); // Update status count
    updateTotal(); // Update total amount
}

function deleteSelectedOrders() {
    var table = document.querySelector("table tbody");
    var checkboxes = table.querySelectorAll('input[type="checkbox"]:checked');

    checkboxes.forEach(function (checkbox) {
        var row = checkbox.closest("tr");
        var status = row.querySelector("td:nth-child(5)").textContent;
        updateStatusCount(status, -1); // Update status count
        table.deleteRow(row.rowIndex);
    });

    updateTotal(); // Update total amount
}

function updateLiveStatus(checkbox) {
    var liveStatus = document.getElementById("liveStatus");
    if (checkbox.checked) {
        liveStatus.textContent = "Order selected: " + checkbox.closest("tr").querySelector("td:nth-child(2)").textContent;
    } else {
        liveStatus.textContent = "No order selected";
    }
}

function updateStatusCount(status, increment) {
    if (status === "received") {
        totalReceived += increment;
        document.getElementById("totalReceived").textContent = totalReceived;
    } else if (status === "delivered") {
        totalDelivered += increment;
        document.getElementById("totalDelivered").textContent = totalDelivered;
    } else if (status === "pending") {
        totalPending += increment;
        document.getElementById("totalPending").textContent = totalPending;
    }
}

function updateTotal() {
    var table = document.querySelector("table tbody");
    var total = 0;

    for (var i = 0; i < table.rows.length; i++) {
        total += parseFloat(table.rows[i].querySelector("td:nth-child(4)").textContent.replace("$", ""));
    }

    document.querySelector(".total p").textContent = "Total: $" + total.toFixed(2);
}
