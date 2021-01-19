const input = require('fs').readFileSync('stdin', 'utf8');
const lines = input.split(' ');
let a = parseFloat(lines.shift())
let b = parseFloat(lines.shift())
let c = parseFloat(lines.shift())
let delta = b **2 - 4 * a * c
let r1, r2
if (delta < 0){
    console.log("Impossivel calcular")
}else{

}



r1 = (-b + (Math.sqrt(delta))) / 2 * a
r2 = (-b - (Math.sqrt(delta))) / 2 * a
console.log(`R1 = ${r1.toFixed(5)}`)
console.log(`R2 = ${r2.toFixed(5)}`)