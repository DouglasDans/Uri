# -*- coding: utf-8 -*-

n1 = input()
list = n1.split(' ')
listInt = []
cont = 0
while cont < len(list):
    listInt.append(int(list[cont]))
    cont +=1
cont = 0

listInt.sort()
while cont < len(listInt):
    print(listInt[cont])
    cont +=1
print("")
cont = 0
while cont < len(listInt):
    print(list[cont])
    cont +=1