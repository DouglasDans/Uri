const input = require('fs').readFileSync('stdin', 'utf8');
const lines = input.split('\n');

const line1 = lines[0].split(' ')

let nota1 = parseFloat(line1.shift())
let nota2 = parseFloat(line1.shift())
let nota3 = parseFloat(line1.shift())
let nota4 = parseFloat(line1.shift())
let exame = parseFloat(lines[1])

media(nota1, nota2, nota3, nota4)

function media(nota1, nota2, nota3, nota4){
    let resultado = 0

    nota1 = nota1 * 2
    nota2 = nota2 * 3
    nota3 = nota3 * 4
    nota4 = nota4 * 1

    resultado = (nota1 + nota2 + nota3 + nota4) / (2 + 3 + 4 + 1)
    console.log("Media: " + resultado.toFixed(1));
    aprovacao(resultado, exame)
}

function aprovacao(media = 0, exame = 0){
    if (media >= 5 && media <= 6.9){
        let mediaFinal = 0

        console.log("Aluno em exame.")
        console.log("Nota do exame: " + exame.toFixed(1));
        
        mediaFinal = (exame + media) / 2

        if (mediaFinal >= 5 ){
            console.log("Aluno aprovado.")
        }else{
            console.log("Aluno reprovado.")
        }

        console.log("Media final: " + mediaFinal.toFixed(1));
    }
    if (media < 5 ){
        console.log("Aluno reprovado.")
    }
    if (media >= 7 ){
        console.log("Aluno aprovado.")
    }
}