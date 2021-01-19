const input = require('fs').readFileSync('stdin', 'utf8');
const lines = input.split('\n');
let linha1 = lines.shift().split(" ")
let linha2 = lines.shift().split(" ")
let resp = 0
for (let i = 0; i < 3; i++){
    if (parseInt(linha1[i]) - parseInt(linha2[i]) < 0){
        resp += parseInt(linha1[i]) - parseInt(linha2[i])
    }
}
if (resp < 0){
    resp *= -1
}
console.log(resp)