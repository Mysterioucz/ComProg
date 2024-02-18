ids = []
grades = []
g=['F','D','D+','C','C+','B','B+','A','A']
c = input()
while c!='q':
    c = c.split()
    ids.append(c[0])
    grades.append(c[1])
    c = input()
uids=input().split()
for i in uids:
    n = ids.index(i)
    grades[n] = g[g.index(grades[n])+1]
for i in range(len(ids)):
    print(ids[i],grades[i])