def row_number(t, e): # return row number of t containing e (top row is row #0)
    for i in range(len(t)):
        if e in t[i]:
            return i
def flatten(t): # return a list of ints converted from list of lists of ints t
    res = []
    for e in t:
        for num in e:
            if num!=0:
                res.append(num)
    return res
def inversions(x): # return the number of inversions of list x
    inv = 0
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            if x[i]>x[j]:
                inv += 1
    return inv
def solvable(t): # return True if tiling t (list of lists of ints) is solvable
 # otherwise return False
    data = flatten(t)
    inv = inversions(data)
    if len(t)%2==0:
        row = row_number(t,0)
        if inv%2==0:
            if row%2==0:
                return False
            else:
                return True
        else:
            if row%2==0:
                return True
            else:
                return False  
    else:
        if inv%2==0:
            return True
        else:
            return False
        
     

exec(input().strip()) # do not remove this line