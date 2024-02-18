n = int(input())
data,step = {},[]
for i in range(n):
    Id,pos = input().split(':')
    step.append(Id)
    data[Id] = pos
key_id = input().strip()
res = set()
if key_id in data:
    for p in data[key_id].split(', '):
        for k,v in data.items():
            if p in v and k!=key_id:
                res.add(k)
    if len(res)>0:   
        for e in sorted(res,key=lambda x:step.index(x)):
            print(e)
    else:
        print("Not Found")