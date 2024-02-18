def is_odd(n):
    if n%2 != 0:
        return True
    else:
        return False

def has_odds(x):
    result  = False
    for e in x:
        if e%2 != 0 :
            result = True
    return result

def all_odds(x):
    result = True
    for e in x:
        if e%2 == 0:
            result = False
    return result

def no_odds(x):
    result = True
    for e in x:
        if e%2 != 0:
            result=False
    return result

def get_odds(x):
    result = []
    for e in x:
        if e%2 != 0 :
            result.append(e)
    return result

def zip_odds(a,b):
    oa,ob,result = [],[],[]
    for e in a:
        if e%2 != 0 :
            oa.append(e)
    for e in b:
        if e%2 != 0 :
            ob.append(e)
    n = max(len(oa),len(ob))
    for i in range (n):
       try:
           result += [oa[i],ob[i]]
       except:
           if len(oa)>len(ob):
                result.append(oa[i])
           else:
                result.append(ob[i])
    return result
exec(input().strip())