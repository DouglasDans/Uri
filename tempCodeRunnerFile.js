const lines = input.split(' ');
const a = parseInt(lines.shift())
const b = parseInt(lines.shift())
const c = parseInt(lines.shift())
const d = parseInt(lines.shift())
if (b > c){
    if (d > a){
        if (c + d > a + b){
            if (c > 0 && d > 0){
                console.log("Valores Aceitos")
            }
        }
    }
}else{
    console.log("Valores nao aceitos")
}