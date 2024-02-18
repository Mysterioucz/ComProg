import numpy as np
# x = np.array([1,2])
# y = np.array([[i,i+1] for i in range(1,7,2)])
# print(y.dot(x),x,y)
# a = {1,2,3,4}
# b = {5,6}
# print(a.union(b),a,len(a))
d = np.array([1,3,10,5,2,10,8,-8])
c = np.arange(49).reshape((7,7))
# print(d.multiply(c))
# print(np.multiply(d,c))
# print(d*c)
class A:
    def __init__(self,a):
        self.a = a
    def get_a(self):
        return self.a
    def triple(self):
        self.a *= 3
    def __str__(self):
        return str(self.a)
x = A(8)
x.a *= 3
print(x)