def factor(n):
    div,c = 2,0
    res = []
    while n != 1:
        if n%div ==0:
            while n%div == 0:
                c+=1
                n /= div
            res.append([div,c])
            c=0
        else:
            div +=1
    return res
exec(input().strip())