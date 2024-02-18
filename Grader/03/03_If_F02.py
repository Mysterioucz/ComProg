def choose(stu1,stu2):
    c1 = 0
    c2 = 0
    Id = []
    if stu1[2] == 'A' and stu1[3]<='C'and stu1[4]<='C':
        c1 += 1
    if stu2[2] == 'A' and stu2[3]<='C'and stu2[4]<='C':
        c2 += 1
    if c1 == 1 and c2 == 1:
        if stu1[1]>stu2[1]:
            Id = [stu1[0]]
        elif stu1[1]<stu2[1]:
            Id = [stu2[0]]
        else:
            if stu1[3]<stu2[3]:
                Id = [stu1[0]]
            elif stu1[3]>stu2[3]:
                Id = [stu2[0]]
            else:
                if stu1[4]<stu2[4]:
                    Id = [stu1[0]]
                elif stu1[4]>stu2[4]:
                    Id = [stu2[0]]
                else:
                    Id = [stu1[0]]+[stu2[0]]
    if c1>c2:
        Id = [stu1[0]]
    elif c1<c2:
        Id = [stu2[0]]
    return Id
exec(input())