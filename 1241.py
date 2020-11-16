a = int(input())

for i in range(0,a):
    num = input()
    numlist = num.split(" ")
    num1 = numlist[0]
    num2 = numlist[1]
    
    if num1[len(num1) - len(num2): len(num1)] == num2:
        print("encaixa")
    else:
        print("nao encaixa")

