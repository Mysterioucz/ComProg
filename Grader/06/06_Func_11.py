x = input().strip().split()
res = int(x[0],2)+int(x[1],2)
print(bin(res)[2::])