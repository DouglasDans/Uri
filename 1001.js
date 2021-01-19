var input = require('fs').readFileSync('stdin', 'utf8');
var lines = input.split('\n');
let a, b, x;
a = parseInt(lines.shift());
b = parseInt(lines.shift());
x = a + b;
console.log(`X = ${x}`);


