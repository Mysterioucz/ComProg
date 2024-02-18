p = [0,'A','2','3','4','5','6','7','8','9','T','J','Q','K']
s = [0,'C','D','H','S']

raw = input().strip()
d,result = [],''
for i in range(0,len(raw),2):
    d.append(raw[i:i+2])
for i in range(len(d)-1):
    if d[i][0] == d[i+1][0]:
        if d[i][1] == d[i+1][1]:
            result += '0'
        else:
             if s.index(d[i][1])- s.index(d[i+1][1])>0:
                result += '+'+str(s.index(d[i][1])- s.index(d[i+1][1]))
             else:
                result += str(s.index(d[i][1])- s.index(d[i+1][1]))
    else:
        if p.index(d[i][0])- p.index(d[i+1][0])>0:
            result += '+'+str(p.index(d[i][0])- p.index(d[i+1][0]))
        else:
            result += str(p.index(d[i][0])- p.index(d[i+1][0]))
print(result)