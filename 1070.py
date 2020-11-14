# -*- coding: utf-8 -*-
x = int(input())
count = 0
if x%2 == 0:
    x += 1
    print(x)
    while count < 5:
        x += 2
        print(x)
        count += 1
else:
    print(x)
    while count < 5:
        x += 2
        print(x)
        count += 1


