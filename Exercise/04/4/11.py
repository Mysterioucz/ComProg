n = int(input())
for i in range(1,n+1):
    print("*"*i)
    if i==n:
        for j in range(n-1,0,-1):
            print("*"*j)