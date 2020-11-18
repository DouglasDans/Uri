a = int(input())
for i in range(0,a):
    dias = 0
    n = float(input())
    while n > 1:
        dias += 1
        n = n * 0.5
    print(str(dias)+" dias")

