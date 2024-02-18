import numpy as np
def read_data():
    w = [float(e) for e in input().split()]
    weight = np.array(w)
    n = int(input())
    data = np.ndarray((n, 4), int)
    for i in range(n):
        data[i] = [int(e) for e in input().split()]
    return weight, data

def report_lower_than_mean(weight, data):
    mean = np.mean(data[:,1:].dot(weight))
    lower= ((data[data[:,1:].dot(weight)<mean])[:,0]).astype(str) #เปลี่ยน datatype ให้เป็น str เพื่อ join
    if len(lower) != 0:print(", ".join(lower))
    else: print("None")
    return 
exec(input().strip()) 