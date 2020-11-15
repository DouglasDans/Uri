# -*- coding: utf-8 -*-

while True:
    
    p = input().split()
    x, y = p

    x = float(x)
    y = float(y)

    if x > 0:
        if y > 0:
            print('primeiro')
        if y < 0:
            print('quarto')
    if x < 0:
        if y > 0:
            print('segundo')
        if y < 0:
            print('terceiro')
    if x == 0 or y == 0:
        break
