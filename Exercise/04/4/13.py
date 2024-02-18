t = input()
c = 0
vowel = "aeiouAEIOU"
for i in range(len(t)):
    if t[i] in vowel:
        c += 1
print(c)