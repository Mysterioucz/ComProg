w = input().strip()
alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
alp2 = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
while w != 'end':
    res =""
    for e in w:
        if e in alp:
            res += alp[alp.index(e)+13]
        elif e in alp2:
            res += alp2[alp2.index(e)+13]
        else:
            res += e
    print(res)
    w = input().strip()