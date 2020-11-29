list = input().split(" ")
p1, c1, p2, c2 = list

valor1 = int(p1) * int(c1)
valor2 = int(p2) * int(c2)

if valor1 == valor2:print("0")
elif valor1 > valor2:print("-1")
else: print("1")