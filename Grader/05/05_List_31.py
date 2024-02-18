c = input().split()
m = input()
h = int(len(c)/2)
for e in m:
    if e=='C':
        c = c[h::1] + c[0:h:1]
    elif e=='S':
        b=c[h::1]
        f=c[0:h:1]
        c = []
        for i in range(len(f)):
             c.append(f[i])
             c.append(b[i])
c = " ".join(c)
print(c)