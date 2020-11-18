contador = int(input())
i = 1
t = 0
j = 1 
while t < contador:
	print(str(i),end=' ')
	if j == 3:
		print("PUM")
		t += 1
		j = 0
		i += 1  
	j += 1 
	i += 1     