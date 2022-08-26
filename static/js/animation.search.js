var data = document.getElementById("data").value;
const rdata = JSON.parse(data.replace(/&quot/g, '"'));
// console.log(rdata);
const input = document.getElementById("search_here");

let filteredArr = [];

input.addEventListener("keyup", (e) => {
  box.innerHTML = "";

  filteredArr = rdata.filter((article) =>
    article["description"].includes(e.target.value)
  );

  if (filteredArr.length > 0) {
    filteredArr.map((article) => {
      box.innerHTML += `<b>${article["fklaw__title"]} - ${article["description"]}</b><br>`;
    });
  } else {
    box.innerHTML = "<b>No result found ..</b>";
  }
});
