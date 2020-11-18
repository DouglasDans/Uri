list = input().split(" ")
a = int(list[0])
b = int(list[1])
for r in range(abs(b)):
    if ((a - r) % b) == 0:
        q = int((a - r)/b)
        break
print(q, r)