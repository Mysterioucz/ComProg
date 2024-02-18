n = int(input())
k = int(input())
def main():
    bit = ['0','1']
    for i in range(n-1):
        bit_reverse = bit[::-1].copy()
        bit = ['0'+e for e in bit]
        bit += ['1'+e for e in bit_reverse]
    ruler = ""
    for j in range(1,k+1):
        if j!=k:
            ruler += str(j)+"-"*((n+1)-len(str(j)))
        else:
            ruler += str(j)+"-"*(n-len(str(j)))
    print(ruler)
    for s in range(0,len(bit),k):
        print(",".join(bit[s:s+k]))
    
if n<0 and k<0:
    print("Invalid n and k")
elif n<0:
    print("Invalid n")
elif k<0:
    print("Invalid k")
else:
    main()
