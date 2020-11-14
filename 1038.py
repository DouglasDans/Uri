# -*- coding: utf-8 -*-

n1 = input()
list = n1.split(' ')
listInt = []
x = 0
while x < len(list):
    listInt.append(int(list[x]))
    x +=1

valor = 0
i = 1
while(i <= listInt[1]):
    if listInt[0] == 1:
        valor += 4.00
    elif listInt[0] == 2:
        valor += 4.50
    elif listInt[0] == 3:
        valor += 5.00
    elif listInt[0] == 4:
        valor += 2.00
    elif listInt[0] == 5:
        valor += 1.50
    i += 1


print("Total: R$ %.2f" % valor)

