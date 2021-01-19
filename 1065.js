const input = require('fs').readFileSync('stdin', 'utf8');
const lines = input.split('\n');
let par = 0
for(let i = 0; i < input.length; i++){
    if (parseInt(lines.shift()) % 2 === 0){
        par++
    }
}
console.log(`${par} valores pares`)






