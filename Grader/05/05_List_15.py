x = [int(e) for e in input().split()]
x.sort()
d=x[0]
c=1
r=[x[0]]
for i in range(len(x)):
    if x[i]!=d:
        c+=1
        r.append(x[i])
        d=x[i]
    else:
        pass
print(c,r[:10:],sep='\n' )