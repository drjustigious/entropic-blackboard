var c = document.getElementById("blackboardCanvas");
var ctx = c.getContext("2d");
ctx.moveTo(0, 0);
ctx.lineTo(200, 100);
ctx.stroke();

let fontSize = 16;

ctx.font = `${fontSize}px "Lucida Console", Monaco, monospace`;
ctx.fillStyle = "rgb(127,127,127)";


let columns = 32;
let rows = 12;
let aspectRatio = 1234.0/2048.0  // Accurate for Lucida Console.

for (let i=0; i<=columns; i++) {
    for (let j=0; j<rows; j++) {
        ctx.fillText("Ä", aspectRatio*fontSize*i, fontSize*j);
    }
}