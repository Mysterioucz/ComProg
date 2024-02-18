import math
n = int(input())
s = []
for i in range(1,n+1,1):
    p = [float(e) for e in input().split()]
    d = math.sqrt(p[0]**2+p[1]**2)
    s.append([d,i,p[0],p[1]])
s.sort()
print('#'+str(s[2][1])+':','('+str(s[2][2])+', '+str(s[2][3])+')')