# -*- coding: utf-8 -*-
n1 = input()
list = n1.split(' ')
listInt = []
x = 0
while x < len(list):
    listInt.append(int(list[x]))
    x +=1

listInt.sort(reverse=True)
valor = listInt[0]
print(str(valor)+" eh o maior")



