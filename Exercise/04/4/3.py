n = int(input())
s = 0
k = 1
for i in range(n,0,-1):
    if i%2 ==0 :
        s+= i*k
    else:
        s -= k
    k +=2
    s+=i*k
print(s)