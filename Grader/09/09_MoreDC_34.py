def pattern1(nrows, ncols):
    if nrows==0 and ncols==0:
        return[]
    elif nrows==1 and ncols==1:
        return[[1]]
    elif nrows==1 and ncols==0:
        return[[]]
    res=[[e for e in range(i,i+ncols)] for i in range(1,ncols*nrows,ncols)]
    return res
        
def pattern2(nrows, ncols):
    res=[[e for e in range(i,i+ncols*nrows,nrows)] for i in range(1,nrows+1)]
    return res
def pattern3( N ):
    res=[]
    if N==0:
        return res
    for i in range(1,int(((N**2)-N)/2+N+1)):
        if len(res)%N == 0 :
            for j in range(len(res)//N):
                res.append(0)
        res.append(i)
    res= [list(map(int,sorted(res[j:j+N]))) for j in range(0,len(res),N)]
    return res
    
def pattern4( N ):
    if N==0:
        return []
    res = [[0 for i in range(N)] for j in range(N)]
    val=int(((N**2)-N)/2+N+1)-1
    for i in range(N-1,-1,-1): #หลัก
        for j in range(0,i+1):#แถว
            res[j][i] = val
            val-=1
    return res
def pattern5( N ):
    if N==0:
        return []
    res = [[0 for i in range(N)] for j in range(N)]
    val=1
    j = 0
    for k in range(N):
        for i in range(N-j): #แนวแทยง
            res[i][i+j] = val
            val += 1
        j+=1
    return res
def pattern6( N ):
    if N==0:
        return []
    res = [[0]*j for j in range(N)]
    val=1
    for i in range(N):
        val += (N-i-1)*(i % 2)
        for j in range(N-i):
            res[j] += [val]
            val += (-1) ** i
        val += (N-i+1)*(i % 2)
    return res
    
exec(input().strip())