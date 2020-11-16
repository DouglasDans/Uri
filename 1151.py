k = int(input())
a = 0
i = 0
ant = 0
p = 1
while i < k:
	if i == 1: ant = 0
	if i >= k - 1:
		print(a)
	else:
		print(a,end=' ')
	a = ant + p
	ant = p
	p = a
	i += 1
