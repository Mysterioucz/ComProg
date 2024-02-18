m = int(input())
b = -m
for i in range(b,m+1,2):
    if i%2 == 0:
        print(i)
    elif i<m :
        i += 1
        print(i)
    
    
