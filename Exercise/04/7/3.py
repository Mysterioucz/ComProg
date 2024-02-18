s = ['@',':','-','+']
x = input()
for i in range(len(x)):
    if x[i] in s:break
b = x.split(x[i])
print(b[0],b[1])