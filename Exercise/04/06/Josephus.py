n = int(input().strip())
circle = ['G']*n + ["B"]*n
res = circle.copy()
for d in range(1,2*n):
    c = d
    while len(res)>1:
        res.pop(c)
        c = (c+d)%len(res)
    if res[0] == 'G':
        print(d)
        break
    else:
        res = circle.copy()
