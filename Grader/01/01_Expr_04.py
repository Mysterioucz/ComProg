import math
w = float(input())
h = float(input())
M = math.sqrt(w*h)/60
H = 0.024265*(w**0.5378)*(h**0.3964)
B = 0.0333*(w**(0.6157-0.0188*math.log(w,10)))*(h**0.3)
print(M)
print(H)
print(B)