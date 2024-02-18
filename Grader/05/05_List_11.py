x = input()
h = []
found = False
for i in range(10):
    if str(i) not in x:
        h.append(str(i))
        found = True
h = ",".join(h)
if not found:
    print("None")
else:
    print(h)