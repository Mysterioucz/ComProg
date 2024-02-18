def T2M(text):
    res = ""
    for ch in text:
        if ch in pattern:
            start = pattern.find(ch)+2
            stop = pattern.find("[",start)
            res += pattern[start:stop]+" "
        else:
            return "Invalid : "+ text
    return res
def M2T(code):
    res = ""
    code = code.split()
    ptt = pattern.replace("["," ").replace("]"," ").split()
    for m in code:
        if m in ptt:
            ch = ptt[ptt.index(m)-1]
            res += ch
        else:
            return "Invalid : "+m
    return res.strip()
name = input().strip()
file = open(name,'r')
method = file.readline().strip()
pattern = file.readline().strip()
line  = file.readline().strip()
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