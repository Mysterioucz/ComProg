import math
c = input().strip()
if c == 'S':
    m = int(input())
    q,r,t,k,n,x,i,p=1,0,1,1,3,3,0,""
    while i<m :
        if 4*q+r-t<n*t:
            p += str(n)
            i += 1
            a = 10*(r-n*t)
            n = 10*(3*q+r)//t-10*n
            q = 10*q
            r = a
        else:
            a = (2*q+r)*x
            b = (7*k*q+2+x*r)//(x*t)
            q = k*q
            t = x*t
            x+=2
            k+=1
            n = b
            r = a
    p = p[0]+'.'+p[1::]
    print('pi =',p)
else:
    if c=='R':
        n = int(input())
        x = 0
        for k in range(n+1):
            x += ((-3)**-k)/(2*k+1)
        p=math.sqrt(12)*x
        p = round(p,12)
        print('pi =',p)
    else:
        if c=='P':
            p = math.sqrt(7+math.sqrt(6+math.sqrt(5)))
            p = round(p,6)
            print('pi =',p)
        else:
            print('Invalid')