# -*- coding: utf-8 -*-
T = input()
list = []
listint = []
n1 = input()
list = n1.split(' ')
i = 0
contador = 0
while i < len(list):
    if T == list[i]:
        contador += 1
    i += 1
print(str(contador))

