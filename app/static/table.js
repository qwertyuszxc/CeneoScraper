var xmlhttp = new XMLHttpRequest();
var url = "";
var data = [];
var objectData = null;

function get_data(file_url) {
  xmlhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        objectData = JSON.parse(this.responseText);
        drawTable(objectData);
    }
};
  xmlhttp.open("GET", file_url, true);
  xmlhttp.send();
}



get_data("https://raw.githubusercontent.com/qwertyuszxc/CeneoScraperS11/main/PP2_fixed.json");


function drawTable() {
  
        let tableData ='';
        objectData.map((values) => {
        tableData+=         `<tr>
        <td>${values.ID}</td>
        <td>${values.Opinii}</td>
        <td>${values.Wady}</td>
        <td>${values.Zalety}</td>
        <td>${values.Ocena}</td>
    </tr>`;
    });
    document.getElementById('table-body').innerHTML=tableData;
}