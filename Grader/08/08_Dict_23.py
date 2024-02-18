def reverse(x):
    res={}
    for k in x:
        res[x[k]]=k
    return res
n = int(input())
data={}
for i in range(n):
    x = input()
    # spliter = x.index('0')
    c=0
    for j in range(len(x)):
        if x[j] == ' ':
            c+=1
            if c == 2:
                spliter = j
                break
    data[x[:spliter].strip()] = x[spliter:].strip()
datar = reverse(data)
n = int(input())
for i in range(n):
    out = input()
    if out in data:
        print(out,'-->',data[out])
    elif out in datar:
        print(out,'-->',datar[out])
    else:
        print(out,'-->','Not found')
# print(data,datar)