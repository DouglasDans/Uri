const input = require('fs').readFileSync('stdin', 'utf8');
const lines = input.split(' ');
const a = parseInt(lines.shift())
const b = parseInt(lines.shift())
const c = parseInt(lines.shift())
const d = parseInt(lines.shift())
if ((b > c) && (d > a) && (c + d > a + b) && (c > 0) && (d > 0)){
    console.log("Valores aceitos")
}else{
    console.log("Valores nao aceitos")
}