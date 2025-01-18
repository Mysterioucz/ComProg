def T2M(text):
    res = ""
    for ch in text:
        if ch in pattern:
            res += pattern[ch]+" "
        else:
            return "Invalid : "+ text
    return res
def M2T(code):
    res = ""
    code = code.split()
    ptt = dict((v,k) for k,v in pattern.items())
    for m in code:
        if m in ptt:
            res += ptt[m]
        else:
            return "Invalid : " + ' '.join(code)
    return res.strip()
name = input().strip()
file = open(name,'r')
method = file.readline().strip()
raw_pattern = file.readline().strip()
pattern = dict()
line  = file.readline().strip()
i = raw_pattern.find("]")
while i != -1 :
    pattern[raw_pattern[i-1]] = raw_pattern[i+1:raw_pattern.find("[",i + 1)]
    i = raw_pattern.find("]",i+1)
if method == "T2M":
    while len(line) != 0:
        print(T2M(line))
        line = file.readline().strip()
elif method == "M2T":
    while len(line) != 0:
            print(M2T(line))
            line = file.readline().strip()
else:
    print("Invalid code")
file.close()