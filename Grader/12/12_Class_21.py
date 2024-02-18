class Complex :
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __str__(self):
        if self.a == 0 and self.b == 0:
            return "0" 
        elif self.a == 0:
            if self.b != 1 and self.b>0:
                return str(self.b)+"i"
            elif self.b<0 :
                if self.b == -1:return "-i"
                return str(self.b)+"i"
            return "i"
        elif self.b == 0:
            return str(self.a)
        elif self.b <0:
            if self.b!=-1 :
                return str(self.a)+str(self.b)+"i"
            return str(self.a)+"-i"
        if self.b!=1:
            return str(self.a)+"+"+str(self.b)+"i"
        return str(self.a)+"+"+"i"
    def __add__(self, rhs):
        return Complex(self.a+rhs.a,self.b+rhs.b)
    def __mul__(self, rhs):
        return Complex(self.a*rhs.a-self.b*rhs.b,self.a*rhs.b+self.b*rhs.a)
    def __truediv__(self, rhs):
        a,b,c,d = self.a,self.b,rhs.a,rhs.b
        return Complex((a*c+b*d)/(c**2+d**2),(-a*d+b*c)/(c**2+d**2))
        
t, a, b, c, d = [int(x) for x in input().split()]
c1 = Complex(a,b)
c2 = Complex(c,d)
if t == 1 : print(c1)
elif t == 2 : print(c2)
elif t == 3 : print(c1+c2)
elif t == 4 : print(c1*c2)
else : print(c1/c2)