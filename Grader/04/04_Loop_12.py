n = int(input())
r = []
h = []
l = []
x = []
y = []
for i in range(n):
    r += list(map(int,input().split()))
m = input()
for i in range(0,2*n,2):
    x += [r[i]]
    y += [r[i+1]]
for i in range(0,n,2):
    l += [x[i]]
    h += [y[i]]
for i in range(1,n,2):
    h += [x[i]]
    l += [y[i]]
if m =='Zig-Zag':
    print(min(l),max(h))
else:
    print(min(h),max(l))
    
    
#Not Work  
# if m =='Zig-Zag':
#     for i in range(1,len(r)-1,3):
#         h += r[i:i+2]
#     l += [r[0]] + [r[len(r)-1]]
#     for i in range(4,len(r)-4,4):
#         l += r[i:i+2]
#         # print(r[i],r[i+3])
#     print(l,h)
#     print(min(l),max(h))
# else:
#     for i in range(1,len(r)-2,3):
#         l += r[i:i+2]
#     for i in range(0,len(r)-3,4):
#         h += r[i] + r[i+3]
#     print(min(l),max(h))