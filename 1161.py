def fatorial(h):

    t = 1
    i = 1
    while (i <= h):
        t = t * i
        i += 1
    return t
    
while True:
    try:
        num = input().split(" ")
        if num[0] == '' or num[1] == '': break
        valor = fatorial(int(num[0])) + fatorial(int(num[1]))
        print(valor)
    except EOFError:break
    






