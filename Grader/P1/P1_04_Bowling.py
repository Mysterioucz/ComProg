raw = input()
n = int(input())
point = []
p = 0
zero = 0
for i in range(len(raw)):
    if raw[i] == 'X':
        if i == len(raw)-2:
            break
        p += 10
        if raw[i+1] == 'X':
            p += 10
        else :
            p += int(raw[i+1])
        if raw[i+2] == 'X':
            p += 10
        elif raw[i+2] == '/':
            p += 10 - int(raw[i+1])
        else:
            p += int(raw[i+2])
        point.append(p)
        p = 0
    elif raw[i] == '/':
        p = 10
        if i == len(raw)-1:
            break
        else:
            if raw[i+1] == 'X':
                p += 10
            else:
                p += int(raw[i+1])
            point.append(p)
            p = 0
        if i == len(raw)-2:
            break
    else:
        if int(raw[i]) == 0:
            zero += 1
        if p == 0:
            if zero == 0:
                p += int(raw[i])
            elif zero == 1:
                if int(raw[i]) != 0:
                    point.append(int(raw[i]))
                    zero = 0
            elif zero == 2:
                point.append(0)
                zero = 0
        else:
            p += int(raw[i])
            point.append(p)
            p = 0
if n > 0 and n <= 10:
    print(point[n-1])
else:
    c = 0
    for e in point:
        c += e
    print(c)