import numpy as np
def peak_indexes(x):
    res = (x[:len(x)-2]<x[1:len(x)-1])&(x[1:len(x)-1:]>x[2:])
    res=np.append(res,False)
    res=np.insert(res,0,False)
    res=np.argwhere(res)
    return res.flatten()
def main():
    d = np.array([float(e) for e in input().split()])
    pos = peak_indexes(np.array(d))
    if len(pos) > 0:
        print(", ".join([str(e) for e in pos]))
    else:
        print("No peaks")
exec(input().strip()) # Don't remove this line
