def check_digit(n):
    total = 0
    for i in range(0,12):
        total = total + (13 - i) * int(n[i])
    return (11 - total%11)%10

exec(input())

# Input : 110290007151 
# Output: 5

# List x = [1,2,3,4,5]
# index     0 1 2 3 4
# x[0]