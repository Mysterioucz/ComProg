def make_int_list(x):
 return list(map(int,x.split()))
def is_odd(e):
 if e%2 != 0:
   return True
 return False
def odd_list(alist):
 res = []
 for e in alist:
     if e %2 != 0:
         res.append(e)
 return res
def sum_square(alist):
 total = 0
 for e in alist:
     total += e**2
 return total
exec(input().strip()) # ต้องมีบรรทัดนี้เมื่อส่งไป grader