    elif not d:
        print(d, c)
    else:
        setdonut = b + c
        cost = b * a
        mindonut = math.ceil(d / setdonut)
        total = mindonut * cost
        alldonut = mindonut * setdonut
        print(total, alldonut)