def is_mobile_number(num):
    p = ['06','08','09']
    if len(num) == 10:
        if num[:2] in p:
            q = True
        else:
            q = False
    else:
        q = False
    return q
exec(input())