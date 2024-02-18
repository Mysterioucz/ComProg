import numpy as np
def eq(A, B, p):
    size = np.size(A)
    eq = np.sum(A==B)*100/size
    return eq>=p
def closest_point_indexes(points, p):
    x,y = points[:,0],points[:,1]
    distance = np.sqrt((p[0]-x)**2+(p[1]-y)**2)
    lowest = np.min(distance)
    return (np.argwhere(distance==lowest)).flatten()
def number_of_inversions(A):
    count = 0
    for i in range(len(A)):
        count += np.sum(A[i+1:]<A[i])
    return count

exec(input().strip())