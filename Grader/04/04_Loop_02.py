a = float(input())
l = 0
u = a
x = (l+u)/2
while(abs(a-10**x)>(1e-10)*max(a,10**x)):
    if 10**x > a:
        u = x
    elif 10**x < a:
        l = x
    x = (l+u)/2
print(round(x,6))
# print('{:.6f}'.format(x)) ถ้าบังคับ 6 ตน