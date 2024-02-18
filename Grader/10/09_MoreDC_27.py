def knows(R,x,y):
    if y in R[x] or x==y:
        return True
    return False
def is_celeb(R,x): 
    for k in R:
        if not knows(R,k,x):
            return False
    if R[x] == set() or x in R[x]:
        return True
    return False
def find_celeb(R):
    for k in R:
        if is_celeb(R,k):
            return k
    return
def read_relations() :
    R = dict()
    while True:
        d = input().split()
        if d[0] == 'q' : break
        if d[0] in R:
            R[d[0]].add(d[1])
        else:
            R[d[0]] = {d[1]}
        if d[1] not in R:
            R[d[1]] = set()
    return R
def main():
    R = read_relations()
    c = find_celeb(R)
    if c == None :
       print('Not Found')
    else:
       print(c)
exec(input().strip()) # do not remove this line