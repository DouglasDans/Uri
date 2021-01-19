n = int(input())
i = 1 
j = 1 
k = 1
h = 0.5
hint = 1
while n > hint:
    print("{} {} {}".format(hint,j,k))
    hint = int(h)
    if h == hint:
        j += 1
        k += 1
    k = k **3
    j = j **2