a = float(input())
l,u = 0,0
d = a
while d != 0:
    d = d//10
    u += 1 
x = (l+u)/2
while abs(a-10**x)>1e-10*max(a,10**x):
    if 10**x>a:
        u = x
    elif 10**x<a:
        l = x
    x = (l+u)/2
print(round(x,6))
