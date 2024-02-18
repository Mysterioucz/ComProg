ids = []
grades = []
g=['F','D','D+','C','C+','B','B+','A','A']
c = input()
r=[]
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
    r.append([ids[i],grades[i]])
r.sort()
for i in r:
    print(i[0],i[1])