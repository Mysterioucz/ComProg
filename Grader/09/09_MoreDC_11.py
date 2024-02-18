n = int(input())
output = ""
for i in range(n):
    line = input().strip()
    if "." in line:
        for j in range(len(line)):
            if line[j]!=".":
                c = j
                break
        resline = line[:j//2]+line[j:]+"\n"
        output += resline
    else:
        output += line + "\n"
print(output)