fname = input().strip()
k = int(input())
ruler = ''
for i in range(k//10) :
 ruler += '-'*9 + str(i+1)
if len(ruler)<k :
 ruler += '-'*(k-len(ruler))
res = [""]
file = open("E:/Chat/University/CU/Study/Com Prog/Grader/P3/Testcase/text_formatting_files/"+fname,'r')
for line in file:
    i=0
    while i < len(line.strip()):
        if len(line.strip()[i:i+k])==k:
            if (i==0 and len(res[-1]+line.strip()[i:line.find(".")])+1<=k)and(res[-1]!=""):
                old_len= len(res[-1])+1
                if line.strip()[i:i+k+1-old_len][-1] == "." or line.strip()[i:i+k-old_len][-1] == ".": #จบพอดี
                    res[-1] += "."+(line.strip()[i:i+k-old_len].strip("."))
                    i += line[i+k-old_len:].find(line.strip()[i+k-old_len:].strip(".")[0])+k-old_len
                else:#จบระหว่างคำอื่น
                    f_pos = line.strip()[i:i+k-old_len].rfind(".")
                    res[-1] += "."+(line.strip()[i:f_pos].strip("."))
                    i += f_pos+1
            else:    
                if line.strip()[i:i+k+1][-1] == "." or line.strip()[i:i+k][-1] == ".": #จบพอดี
                    res.append(line.strip()[i:i+k].strip("."))
                    if i+k >= len(line.strip().strip(".")):break
                    else:i += line[i+k:].find(line.strip()[i+k:].strip(".")[0])+k
                else:#จบระหว่างคำอื่น
                    f_pos = line.strip()[i:i+k].rfind(".")
                    if f_pos != -1:
                        res.append(line.strip()[i:i+f_pos].strip("."))
                        i += f_pos+1
                    else:
                        if (len(res[-1]+line.strip()[i:]) <= k) and (res[-1]!=""):
                            res[-1] += "."+line.strip()[i:]
                            break
                        else:#คำยาวเกิน k
                            f_pos2 = line.strip()[i:].find(".")
                            if f_pos2 != -1:
                                res.append(line.strip()[i:i+f_pos2].strip("."))
                                i += f_pos2+1
                            else:
                                res.append(line.strip()[i:].strip("."))
                                break
        else:
            if line.find(".") != -1:
                if (i==0 and len(res[-1]+line.strip()[i:line.find(".")])+1<=k)and(res[-1]!=""):
                    old_len= len(res[-1])+1
                    if line.strip()[i:i+k+1-old_len][-1] == "." or line.strip()[i:i+k-old_len][-1] == ".": #จบพอดี
                        res[-1] += "."+(line.strip()[i:i+k-old_len].strip("."))
                        i += line[i+k-old_len:].find(line.strip()[i+k-old_len:].strip(".")[0])+k-old_len
                    else:#จบระหว่างคำอื่น
                        if len(res[-1]+line.strip())+1<=k:
                            res[-1] += "."+ line.strip()
                            break
                        else:
                            f_pos = line.strip()[i:i+k-old_len].rfind(".")
                            if f_pos != -1:
                                res[-1] += "."+(line.strip()[i:f_pos].strip("."))
                                i += f_pos+1
                            else:
                                res.append(line.strip())
                                break
                else:
                    if (len(res[-1]+line.strip()[i:].rstrip("."))+1<=k) and (res[-1]!=""):
                        res[-1] += "."+line.strip()[i:].rstrip(".")
                        break
                    else:
                        if len(line.strip()[i:].strip(".")) <= k: 
                            res.append(line.strip()[i:].strip("."))
                            break
                        else:
                            res.append(line.strip()[i:i+k].strip("."))
                            i += k
            else:#ทั้งบรรทัดไม่มีจุดเลย
                if (i==0 and len(res[-1]+line.strip())<=k)and(res[-1]!=""):#จบพอดี
                    res[-1] += "."+(line.strip()[i:].strip("."))
                    break
                else:
                    res.append(line.strip()[i:].strip())
                    break
res.pop(0)
print(ruler)
for e in res:
    print(e.strip())