onion = set()
n = int(input())
for i in range(n):
    data = set([int(e) for e in input().split()])
    onion = onion.union(data)
    if i ==0:
        inter = data
    else:inter = inter.intersection(data)
if n==0:
    print(0)
    print(0)
else:
    print(len(onion))
    print(len(inter))