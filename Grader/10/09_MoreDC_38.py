route = {}
data = input().split()
while len(data) >1:
    if data[0] in route:
        route[data[0]].add(data[1])
        if data[1] in route:
            route[data[1]].add(data[0])
        else:
            route[data[1]] = {data[0]}
    else:
        route[data[0]] = {data[1]}
        if data[1] in route:
            route[data[1]].add(data[0])
        else:
            route[data[1]] = {data[0]}
    data = input().split()
start = data[0]
res = {start} # ให้เป็น set เพราะไม่ควรซ้ำ
if start in route:
    res |=  route[start]
    for s1 in route[start]:
        res |= route[s1]
for e in sorted(res):
    print(e)