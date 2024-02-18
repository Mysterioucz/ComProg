def spiral_square(n): # n is a positive odd number
    num = n**2
    s = [[0]*n for _ in range(n)]
    right,left = n,0
    top,bot = 0,n
    lap = int(n/2+0.5)
    for _ in range(lap):
        for c in range(right-1,left-1,-1):
            s[bot-1][c] = num
            num -= 1
        bot -= 1
        for r in range(bot-1,top-1,-1):
            s[r][left]=num
            num -= 1
        left += 1
        for c in range(left,right,1):
            s[top][c] = num
            num -=1
        top += 1
        for r in range(top,bot,1):
            s[r][right-1] = num
            num -= 1
        right -= 1
    return s
def print_square(S):
    for i in range(len(S)):
        print(' '.join([(2*' '+str(e))[-3:] for e in S[i]]))
exec(input().strip())