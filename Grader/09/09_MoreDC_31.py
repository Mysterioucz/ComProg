def gcd(a,b):
 while b != 0:
    a,b = b, a%b
 return a
def is_coprime(a, b, c):
 ab = gcd(a,b)
 div = gcd(ab,c)
 if div == 1:
     return True
 else:
     return False
def primitive_Pythagorean_triples(max_len):
 triple = []
 for a in range(1,max_len+1):
     for b in range(a,max_len+1):
         for c in range(b,max_len+1):
            cop = is_coprime(a,b,c)
            if cop and a**2+b**2==c**2:
                triple.append([a,b,c])
 return sorted(triple,key=lambda x:(x[2],x[0]))
exec(input().strip()) 