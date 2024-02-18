n = int(input())
s = 0
k = 0
while k<n :
    x = int(input())
    if x<0 : break
    else :
        s += x*k
        k += 1
print(s)