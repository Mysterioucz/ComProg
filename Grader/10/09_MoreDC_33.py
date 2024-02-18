def t_to_d(x):
    res = {}
    for e in x:
        res[e[1]] = e[0]
    return res
def add_poly(p1, p2):
    if len(p1)==0 and len(p2)==0:
        return []
    max_degree = max([e[1] for e in p1]+[e[1] for e in p2])
    p1c,p2c  = t_to_d(p1),t_to_d(p2)
    res = []
    for i in range(max_degree+1):
        if i in p1c:
            if i in p2c:
                if p1c[i]+p2c[i] !=0:
                    res += [(p1c[i]+p2c[i],i)]
            else:
                res += [(p1c[i],i)]
        elif i in p2c:
            res += [(p2c[i],i)]
    return res[::-1]
def mult_poly(p1, p2):
    p1c,p2c  = t_to_d(p1),t_to_d(p2)
    res = {}
    for x1 in p1c:
        for x2 in p2c:
            if x1+x2 in res:
                res[x1+x2] += p1c[x1]*p2c[x2]
            else:
                res[x1+x2] = p1c[x1]*p2c[x2]
    return [(res[k],k) for k in sorted(res,reverse=True)]
for i in range(3):
    exec(input().strip())