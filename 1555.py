a = int(input())
for i in range(0,a):
    list = input().split(" ")
    x = int(list[0])
    y = int(list[1])
    r = (3*x)**2 + y**2
    b = 2*(x*2) + (5*y)**2
    c = -100*x + y**3
    listC = []
    listC.append(r)
    listC.append(b)
    listC.append(c)
    listC.sort(reverse=True)
    if listC[0] == r: print("Rafael ganhou")
    if listC[0] == b: print("Beto ganhou")
    if listC[0] == c: print("Carlos ganhou")
