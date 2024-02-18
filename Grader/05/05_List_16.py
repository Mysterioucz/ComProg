n = int(input())
r = [str(n)]
while n!=1:
    if n%2 == 0:
        n/=2
    else:
        n=3*n+1
    r.append(str(int(n)))
r = "->".join(r[-15::])
print(r)