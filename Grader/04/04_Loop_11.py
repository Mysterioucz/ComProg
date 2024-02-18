s = input()
c = 1
r = ''
for i in range(len(s)):
    if i != len(s)-1:
        if s[i] == s[i+1]:
            c += 1
        else:
            r += s[i] + ' '+ str(c) + ' '
            c = 1   
    else:
        if s[i] == s[i-1]:
            r += s[i] +' '+ str(c)+' '
        else:
            r += s[i] +' '+ '1'+' '
print(r)
#Key
# s = input()
# e = s[0]
# c = 1
# out = ''
# for x in s[1:]:
#     if x== e:
#         c+= 1
#     else:
#         out += e+' '+str(c)+' '
#         e = x
#         c = 1
# out += e+' '+str(c)
# print(out)