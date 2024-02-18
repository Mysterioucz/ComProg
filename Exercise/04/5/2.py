t = input()
s = ""
for c in t:
    if c in ",.()":
        s += " "
    else:
        s += c
print(s)