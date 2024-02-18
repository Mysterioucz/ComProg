x=['F','D','D+','C','C+','B','B+','A','A']
def index_of(grades, ID):
    r = -1
    for e in grades:
        if ID in e:
            r = grades.index(e)
    return r
            
def upgrade(grades, IDs):
    for e in IDs:
        for i in range(len(grades)):
            if e in grades[i]:
                n = x.index(grades[i][1])
                grades[i][1] = x[n+1]
    grades.sort()      
# DON'T remove the following three lines
exec(input())
exec(input())
exec(input())