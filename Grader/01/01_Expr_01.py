import math
n = int(input())
l = (math.sqrt(2*math.pi))*(n**(n+1/2))*(math.e**((-n)+(1/(12*n+1))))
u = (math.sqrt(2*math.pi))*(n**(n+1/2))*(math.e**((-n)+(1/(12*n))))
print(l)
print(u)
                                       