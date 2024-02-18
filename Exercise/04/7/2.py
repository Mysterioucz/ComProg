n = int(input())
s = 0
for k in range(n):
    x = int(input())
    if x<0 : break
    else :
        s += x*k
print(s)