n = int(input())
x = []
r =[]
for i in range(n):
    x += [int(input())]
x += [int(e) for e in input().split()]
c = [int(input())]
while c != [-1]:
    x += c
    c = [int(input())]
for i in range(len(x)):
    if i%2 ==0:
        r.append(x[i])
    else:
        r.insert(0,x[i])
print(r)