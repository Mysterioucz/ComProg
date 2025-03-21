a1,a2,p2 = [float(e) for e in input().split()]
p1,v1,v2,t = [0.0,0.0,0.0,0]
if(a1 <= a2):
    print("Not possible")
    exit()
while p1 < p2:
    p1 += 0.5*a1 + v1
    v1 += a1
    p2 += 0.5*a2 + v2
    v2 += a2
    t += 1
print(t,round(p1,2))