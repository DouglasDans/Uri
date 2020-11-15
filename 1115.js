let f = 0 
while (f < 9){
    
    p = require()
    let p = p.split()
    x, y = p

    x = float(x)
    y = float(y)

    if (x > 0){
        if (y > 0){
            print('primeiro')
        }
        if (y < 0){
            print('quarto')
        }
    }
    if (x < 0){
        if (y > 0){
            print('segundo')
        }
        if (y < 0){
            print('terceiro')
        }
    }
    if (x == 0 && y == 0){
        break
    }
        
}