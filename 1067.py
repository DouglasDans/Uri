# -*- coding: utf-8 -*-
x = int(input())
count = 1
print(count)
while True:
    count += 2
    print(count)
    if not (count < x-1):
        break

