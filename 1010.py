# -*- coding: utf-8 -*-
n1 = input()
n2 = input()

list = n1.split(' ')
list2 = n2.split(' ')

valor1 = int(list[1]) * float(list[2])
valor2 = int(list2[1]) * float(list2[2])
resp = valor1 + valor2
print("VALOR A PAGAR: R$ %.2f" % resp)


