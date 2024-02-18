file_name = input().strip()
method = input().strip()
file = open(file_name,'r')
pos,data = set(),[]
for line in file:
    data.append(line.strip())
    for i in range(len(line.strip())):
        if line[i] != ".":
            pos |= {i}     
pos = sorted(pos)
print(pos)
if method == "LSTRIP":
    for e in data:
        print(e[pos[0]:])
elif method == "RSTRIP":
    for e in data:
        print(e[:pos[-1]+1])
elif method == "STRIP":
    for e in data:
        print(e[pos[0]:pos[-1]+1])
elif method == "STRIP_ALL":
    for e in data:
        print("".join([e[ch] for ch in pos]))
else:
    print("Invalid command")
file.close()