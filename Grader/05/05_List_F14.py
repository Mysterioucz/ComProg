def peaks(x):
 # x: list of floats (or ints)
 # returns: list of indexes of peaks
 r = []
 for i in range(1,len(x)-1):
     if x[i] > x[i-1] and x[i]>x[i+1]:
         r.append(i)
 return r
exec(input()) # DON'T remove this line