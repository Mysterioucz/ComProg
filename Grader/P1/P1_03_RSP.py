m = int(input())
c_1,c_2,c_r = 0,0,0
while (c_1 != m and c_2 !=m) and c_r < 3*m:
    p1,p2 = input().split()
    if p1 == p2:
        c_1 += 0
    elif p1 == "R":
        if p2 == "S":
            c_1 += 1
        else:
            c_2 += 1
    elif p1 == "P":
        if p2 == "R":
            c_1 += 1
        else:
            c_2 += 1
    elif p1 == "S":
        if p2 == "P":
           c_1 += 1
        else:
           c_2 += 1      
    c_r += 1
print(c_1,c_2)
if (c_1 !=m and c_2 !=m) or c_1 == c_2:
    print('Tie')
elif c_1>c_2:
    print("Player 1 wins")
else:
    print("Player 2 wins")