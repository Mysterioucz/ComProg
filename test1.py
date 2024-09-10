# def check(s1,s2):
#     if len(s1) != len(s2):
#         print("Invalid answer")
#         return;
#     count = 0
#     for i in range(len(s1)): # A B C D E A A A // Sol[-1]
#         if s1[i] == s2[i]:   # A A C D E B B B // Ans
#             count += 1       # 0 1 2 3 4 5 6 7
#     return count;            # -8 -7 -6 -5 -4 -3 -2 -1

# s1 = input()
# s2 = input()
# check(s1,s2)

# # While Loop
# # For Loop
# n = int(input())
# for i in range(1,n+1):
#     if i == 1:
#         print("."*(n-1) + "*")
#     elif i == n :
#         print("*" * (2*n-1))
#     else:
#         print("." * (n-i) + "*" + "." * (2*(i-1)-1) + "*")