import math
a = float(input())
b = float(input())
c = float(input())
x = ((-b)-math.sqrt(b**2-(4*a*c)))/(2*a)
y = ((-b)+math.sqrt(b**2-(4*a*c)))/(2*a)
print(round(x,3),round(y,3))