for i in range(0, True):
    n = int(input())
    if n == 0: break
    j = 0 
    valor = []
    while n > 1 :
        n = n / 2
        valor = n % 2 
        print(int(valor),end="")
        j += 1
