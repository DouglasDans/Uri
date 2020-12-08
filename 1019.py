n = int(input())
h = 0
m = 0
s = 0 
h = int(n / 3600)
n -= h * 3600
m = int(n / 60)
n -= m * 60
s = int(n)
print(str(h)+":"+str(m)+":"+str(s)+"")