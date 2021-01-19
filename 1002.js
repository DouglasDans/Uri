var input = require('fs').readFileSync('stdin', 'utf8');
var lines = input.split('\n');
let area, resp;
area = parseFloat(lines.shift());
resp = 3.14159 * (area*area)
console.log("A="+resp.toFixed(4))
