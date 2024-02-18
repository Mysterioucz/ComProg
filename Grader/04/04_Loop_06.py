h = int(input())
b = 2*h-1
for i in range(1,h+1):
    if i == 1:
        print((h-i)*"." + "*")
    elif i != h:
        print((h-i)*"." + "*" + "."*(2*i-3)+"*")
    else:
        print("*"*b)