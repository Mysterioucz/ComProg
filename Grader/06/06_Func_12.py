def is_prime(n):
 if n <= 1:
    return False
 for k in range(2,int(n**0.5)+1):
    if n%k == 0:
        return False
 return True
def next_prime(N):
 x,i = N,1
 found = False
 while not found:
     if not is_prime(x+i):
         i += 1
     else:
         return x+i

def next_twin_prime(N):
 i,c = 1,True
 while c:
     if is_prime(N+i) and is_prime(N+i+2):
         c = False
     else:
         i += 1
 return N+i, N+i+2

exec(input().strip()) # ตอ้ งมคี าสั่งนี้ ตรงนี้ตอนสง่ ให้Grader ตรวจ