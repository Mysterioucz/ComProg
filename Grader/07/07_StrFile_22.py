w1 = input().strip().lower()
w2 = input().strip().lower()
def check(x,y):
    check = ""
    for e in x:
        if e not in check:
            check += e
    for e in y:
        if e not in check:
            check += e
    return check
def count(x,w):
    return x.count(w)
res = 'NO'
for e in check(w1,w2):
    if count(w1,e) == count(w2,e):
        res = 'YES'
    else:
        res = 'NO'
print(res)