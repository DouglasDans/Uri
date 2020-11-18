# -*- coding: utf-8 -*-
a = int(input())
c = 0
r = 0
s = 0
for i in range(0,a):
    list = input()
    list = list.split(" ")
    if list[1] == "C":
        c += int(list[0])
    elif list[1] == "R":
        r += int(list[0]) 
    elif list[1] == "S":
        s += int(list[0])
print("Total: "+str(c+r+s)+" cobaias")    
total = c+r+s
print("Total de coelhos: "+str(c))
print("Total de ratos: "+str(r))
print("Total de sapos: "+str(s))
print("Percentual de coelhos: %.2f" % ((100*c)/total)+" %")
print("Percentual de ratos: %.2f" % ((100*r)/total)+" %")
print("Percentual de sapos: %.2f" % ((100*s)/total)+" %")
