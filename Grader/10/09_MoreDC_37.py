n = int(input())
depart = {}
for i  in range(n):
    dep = input().split()
    depart[dep[0]] = int(dep[1])
n = int(input())
data = []
for i in range(n):
    data.append(input().split())
data.sort(reverse=True,key=lambda x:float(x[1]))
res = []
for e in data:
    st_dep = e[-4:]
    for d in st_dep:
        if depart[d] >0:
            res.append([e[0],d])
            depart[d] -= 1
            break
for e in sorted(res):
    print(" ".join(e))
