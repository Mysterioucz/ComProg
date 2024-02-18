method = input()
n = int(input())
d,r = [],[]
temp = ''
valid = True
for i in range(n):
    d.append(input().strip())
c = len(d[0])
for e in d:
    if len(e) != c:
        valid = False
if valid:
    if method == '90':
        for i in range(c):
            for e in d[::-1]:
                temp += e[i]
            r.append(temp)
            temp = ''
    elif method == 'flip':
        for e in d:
            r.append(e[::-1])
    else:
        for e in d[::-1]:
            r.append(e[::-1])
    for e in r:
        print(e)
else:
    print('Invalid size')