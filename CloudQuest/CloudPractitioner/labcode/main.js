'use strict';

$(document).ready(function (){
    console.log("dentro do ready");
    $.ajax({
        type: "GET",
        url: "target-file.csv",
        dataType: "text",
        success: function(data) {processData(data);}
    });
});

function processData(csv){
    let csvLines = csv.split(/\r\n|\n/);
    let headers = csvLines[0].split(',');
    let elGenerate = '<table><tr><th>Hour of the Day</th><th>Wave Length</th></tr>';

    for (let i=1; i<csvLines.length; i++) {
        var data = csvLines[i].split(',');
        if (data.length == headers.length) {
            var arr = [];
            for (var j=0; j<headers.length; j++) {
                let strOut = "<!-- Table Generate -->\n";
                if(j % 2 == 0){
                    strOut = strOut.concat(`<tr><td> ${data[j]} </td>`);
                }else{
                    strOut = strOut.concat(`<td> ${data[j]} meter(s) </td></tr>`);
                }
                elGenerate = elGenerate.concat(strOut);
            }
        }
    }
    let elout = document.getElementById("output");
    elout.insertAdjacentHTML('beforeend', elGenerate);
}