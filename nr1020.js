var input = require('fs').readFileSync('stdin', 'utf8');
var lines = input.split('\n');
let nDias = parseInt(lines.shift());
let ano = 0 , mes = 0;
while (nDias > 1){
    if (nDias >= 365) {
        ano++;
        nDias -= 365;
    }
    if (nDias >= 30){
        mes++;
        nDias -= 30
    }
    if (nDias < 30){
        break;
    }
}
console.log(`${ano} ano (s)`);
console.log(`${mes} mes (es)`);
console.log(`${nDias} dias (s)\n`);
