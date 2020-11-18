a = int(input())
for i in range(0,a):
    led = 0
    num = list(input())
    for k in range(0,len(num)):
        if num[k] == "1": led += 2
        if num[k] == "2": led += 5
        if num[k] == "3": led += 5
        if num[k] == "4": led += 4
        if num[k] == "5": led += 5
        if num[k] == "6": led += 6
        if num[k] == "7": led += 3
        if num[k] == "8": led += 7
        if num[k] == "9": led += 6
        if num[k] == "0": led += 6
    print(str(led)+" leds")


