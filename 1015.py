import math
p1 = input().split(" ")
p2 = input().split(" ")
x = 0 
p1int = []
p2int = []
while x < len(p1):
    p1int.append(float(p1[x]))
    x +=1
x = 0
while x < len(p2):
    p2int.append(float(p2[x]))
    x +=1

valor = math.sqrt(((p2int[0] - p1int[0])**2) + ((p2int[1] - p1int[1])**2))

print("%.4f"% valor)