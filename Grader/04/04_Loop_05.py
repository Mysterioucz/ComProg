w = input()
s = input().replace("/"," ").replace("("," ").replace(")"," ").replace(","," ").replace("."," ").replace("'"," ").replace('"'," ").split()
c = 0
for i in s:
    if w == i:
        c += 1
print(c)


# c = 0
# for i in range(len(s)-len(w)):
#     if w == s[i:i+len(w)]:
#         c += 1
    
# print(c)
 