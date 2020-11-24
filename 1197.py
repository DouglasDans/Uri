while True:
    try:
        line = input().split(" ")
        if line[0] == '':break
        if line[1] == '':break
        v, t = line
        a = (int(v) * int(t))*2
        print(a)
    except EOFError:
        break