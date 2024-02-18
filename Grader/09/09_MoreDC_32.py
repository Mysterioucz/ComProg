def first_fit(L, e):
    for i in range(len(L)):
        if e+sum(L[i])<=100:
            L[i].append(e)
            return
    L.append([e])
def best_fit(L, e):
    res = sorted(L,key=lambda x:sum(x),reverse=True)
    for i in range(len(res)):
        if sum(res[i])+e <=100:
            L[L.index(res[i])].append(e)
            return
    L.append([e])
    
def partition_FF(D):
    res = []
    # for i in range(len(res)):
    #     for e in D:
    #         if e+sum(res[i]) <=100:
    #             res[i].append(e)
    #         else:
    #             res.append([e])
    for val in D:
        first_fit(res,val)
    return res
        
def partition_BF(D):
    res = []
    for val in D:
        best_fit(res,val)
    return res  
exec(input().strip()) 