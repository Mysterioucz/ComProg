def missing_digits(t):
    r=[]
    for i in range(10):
        if str(i) in t:
            pass
        else:
            r.append(i)
    r.sort()
    return r
exec(input()) # DON'T remove this line