# -*- coding: utf-8 -*-
n1 = input()
list = n1.split(' ')
valor = 0
i = 0
while(i < 5):
    if i == 0:
        valor = (float(list[0]) * float(list[2]))/2
        print("TRIANGULO: %.3f" % valor)
    elif i == 1:
        valor =  3.14159 * float(list[2]) ** 2
        print("CIRCULO: %.3f" % valor)
    elif i == 2:
        valor = (float(list[2]) * (float(list[0]) + float(list[1]))) / 2
        print("TRAPEZIO: %.3f" % valor)
    elif i == 3:
        valor = float(list[1]) ** 2
        print("QUADRADO: %.3f" % valor)
    elif i == 4:
        valor = float(list[0]) * float(list[1])
        print("RETANGULO: %.3f" % valor)
    i += 1

