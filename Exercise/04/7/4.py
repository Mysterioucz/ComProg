s = ['@',':','-','+']
x = input()
for i in range(len(x)):
    if x[i] in s: 
        b = x.split(x[i])
        print(b[0],b[1])
        break
if i == len(x)-1:
    print(x)