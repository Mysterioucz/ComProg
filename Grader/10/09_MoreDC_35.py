def filter(d,f):
    res= []
    for e in d:
        if f in e:
            if f != e[0]:
                res.append(e)
    return res
n = int(input())
data = []
for i in range(n):
    data.append(input().split())
find = input().split()
sol = data.copy()
for k in find:
    sol = filter(sol,k)
sol.sort()
if sol==[]:
    print("Not Found")
else:
    for e in sol:
        print(" ".join(e))
