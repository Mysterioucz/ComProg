n,k = [int(e) for e in input().split()]
if n%2 != 0 :
    sa,sb,sc,m = 0,0,0,0
    while m<k:
        a,b,c = list(map(int,input().split()))
        if a==b:
            if a==c:
                if a+b > k:
                    sa += 1
                    sb += 2
                    sc -= 3
                else:
                    sa -= 3
                    sb -= 2
                    sc += 1
            else:
                sa += 2
                sb -= 3
        m += 1
    print(sa,sb,sc)
else:
    s,t = list(map(int,input().split()))
    x = s
    y = t
    if s>t:
        x = s-t
    elif s<t :
        y = 2*(t-s)
    if x+y > k :
        x,y=y,x
        x = y + s**2
    print(x,y)
                