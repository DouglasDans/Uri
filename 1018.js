
var input = require('fs').readFileSync('stdin', 'utf8');
var lines = input.split('\n');

let valor = parseInt(lines.shift())

console.log(valor);

quantidadeNotas(valor, [100, 50, 20, 10, 5, 2 ,1])

function quantidadeNotas(valor, cedula){
    let i
    if (Array.isArray(cedula)){
        cedula.forEach((cedulaAtual) =>{
            for(i = 0; valor >= cedulaAtual; i++){
                valor = valor - cedulaAtual    
            }
            console.log(`${i} nota(s) de R$ ${cedulaAtual},00`)
        })
    }    
}

//Ta certo mas a uri não roda função?
