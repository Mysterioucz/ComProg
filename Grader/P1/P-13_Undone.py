def convex_polygon_area(p):
    n = len(p)
    sum = 0
    for i in range(n):
        try:
            sum += (p[i][0]*p[i+1][1])-(p[i][1]*p[i+1][0])
        except:
            sum += (p[i][0]*p[0][1])-(p[i][1]*p[0][0])
    area = 0.5*sum
    return area
def is_heterogram(s):
    constant = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for e in s:
        if e in constant:
            c+=1
    if c == 1:
        return True
    else:
        return False
#TODO replace_ignorecase,top3(votes)
def replace_ignorecase(s, a, b):
    result,s_low,a_low = list(s),s.lower(),a.lower()
    c = 0
    for i in range(s_low.count(a_low)):
        pos = s_low.index(a_low,c)
        for e in range(len(a)):
            result.pop(pos)
        result.insert(pos,b)
        c = pos+len(a)
    result = "".join(result)
    return result
# def top3(votes):



for k in range(2):
 exec(input().strip())
