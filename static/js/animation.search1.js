var data = document.getElementById("data").value;
var title = document.getElementById("title").value;

let result = title.replace(/\'|\[|\]/gi, "");

let arr = result.split(",");

const rdata = JSON.parse(data.replace(/&quot/g, '"'));
const input = document.getElementById("search_here");

let filteredArr = [];

input.addEventListener("keyup", (e) => {
  box.innerHTML = "";
  filteredArr = rdata.filter((article) =>
    article["description"].includes(e.target.value)
  );
  if (filteredArr.length > 0) {
    filteredArr.map((article) => {
      addTitle("box", arr);
      addRow("box", article);
    });
  } else {
    box.innerHTML = "<b>No result found ..</b>";
  }
});

function addTitle(tableID, title) {
  var table = document.getElementById(tableID);
  var rowCount = table.rows.length;
  var row = table.insertRow(rowCount);
  var cell1 = row.insertCell(0);
  var title1 = title[0];
  cell1.innerHTML = title1;
  var cell2 = row.insertCell(1);
  var title2 = title[1];
  cell2.innerHTML = title2;
  var cell3 = row.insertCell(2);
  cell3.innerHTML = title[2];
  var cell4 = row.insertCell(3);
  cell4.innerHTML = title[3];
}

function addRow(tableID, article) {
  var table = document.getElementById(tableID);
  var rowCount = table.rows.length;
  var row = table.insertRow(rowCount);
  var cell1 = row.insertCell(0);
  var element1 = article["fklaw__title"];
  cell1.innerHTML = element1;
  var cell2 = row.insertCell(1);
  var element2 = article["fkchapter__description"];
  cell2.innerHTML = element2;
  var cell3 = row.insertCell(2);
  cell3.innerHTML = article["num"];
  var cell4 = row.insertCell(3);
  cell4.innerHTML = article["description"];
}
