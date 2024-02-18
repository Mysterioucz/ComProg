t = input()
s = input()
c = 0
for i in range(len(t)):
    if s == t[i:i+len(s)]:
        c += 1
print(c)