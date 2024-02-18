text = input().strip()
char = {}
res = []
for e in text.lower():
    if e not in char and e.isalpha():
        char[e] = text.lower().count(e)
for k in char:
    res.append([-char[k],k])
res.sort()
for e in res:
    print(e[1],'->',-e[0])