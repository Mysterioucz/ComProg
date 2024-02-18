sp ="\"\'/\\,.:;()[]{}@#$%^&*-><"
w = input().strip()
for e in sp:
    w = w.replace(e," ")
w= w.split()
res = w[0].lower()
for i in range(1,len(w)):
    try:
        res += w[i][0].upper() + w[i][1:].lower()
    except:
        res += w[i]
print(res)