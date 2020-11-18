while True:
    try:
        line = input().split(" ")
        n1, n2 = line 
        print(abs(int(n1) - int(n2)))
    except EOFError:
        break