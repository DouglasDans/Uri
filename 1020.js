const input = require('fs').readFileSync('stdin', 'utf8');
const lines = input.split(' ');

let idadeDias = parseInt(lines.shift())
let anos = 0
let meses = 0

while (idadeDias >= 365){
    anos++
    idadeDias -= 365
}
while (idadeDias >= 30){
    meses++
    idadeDias -= 30
}

console.log(anos + " ano(s)");
console.log(meses + " mes(es)");
console.log(idadeDias + " dia(s)");
