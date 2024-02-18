import string
def convex_polygon_area(p):
    x,y= [],[]
    for e in p:
        x.append(e[0])
        y.append(e[1])
    area = 0
    for i in range(len(p)):
        area += 0.5*((x[i-1]*y[i])-(y[i-1]*x[i]))
    return abs(area)
def is_heterogram(s):
    for ch in string.ascii_lowercase:
        if s.lower().count(ch)>1:
            return False
    return True    
def replace_ignorecase(s, a, b):
    res = ""
    i=0
    while i < len(s):
        if s.lower()[i:i+len(a)] == a.lower():
            res += b
            i += len(a)
        else:
            res += s[i]
            i+=1
    return res
def top3(votes):
    res = sorted(votes.keys()) #เรียงตามKey
    top3 = sorted(votes.values(),reverse = True)[:3] #หาคะแนนมากสุด 3 คะแนน
    name = []
    c=0
    while c<3:
        for k in list(res): #กันไม่ให้ grader เอ๋อ(Grader python เก่า)
            if votes[k] == top3[c] and k not in name:
                name.append(k)
        
        c+=1
    return name[:3]
for k in range(2):
 exec(input().strip())
