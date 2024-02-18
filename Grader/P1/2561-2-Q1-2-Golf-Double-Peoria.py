import math
par,stk,adj = 0,0,0
for i in range(9):
    x = list(map(int,input().split()))
    par += x[0]
    stk += x[1]
    if x[2] == 1:
        adj += min(x[1],x[0]+2)
p = math.floor(0.8*(1.5*adj-par))
sum = stk - p
print(stk)
print(p)
print(sum)
