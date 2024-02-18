order = input().strip().split()
timespent = [1,3,7,14]
res = []
while order != ["END"]:
    dim = [31,28,31,30,31,30,31,31,30,31,30,31]
    order[2:] = [int(e) for e in order[2:]]
    if order[4]>=2558:
        if 0<order[3]<13:
            if order[3] == 2 and ((order[4]-543)%400 ==0 or ((order[4]-543)%4 ==0 and (order[4]-543)%100!=0)):
                dim [1] = 29
            if 0<order[2]<=dim[order[3]-1]:
                if order[1] in "EQNF":
                    order[2] += timespent["EQNF".find(order[1])]
                    if order[2] > dim[order[3]-1]:
                        order[2] -= dim[order[3]-1]
                        order[3] += 1
                        if order[3] > 12:
                            order[3] =1
                            order[4] +=1
                    order[2:] = [str(e) for e in order[2:]]
                    # res.append(order[0]+": delivered on "+"/".join(order[2:]))
                    res.append(order)
                else:
                    order[2:] = [str(e) for e in order[2:]]
                    print("Error:"," ".join(order),"-->","Invalid delivery type")
            else:
                order[2:] = [str(e) for e in order[2:]]
                print("Error:"," ".join(order),"-->","Invalid date")
        else:
            order[2:] = [str(e) for e in order[2:]]
            print("Error:"," ".join(order),"-->","Invalid month")
    else:
        order[2:] = [str(e) for e in order[2:]]
        print("Error:"," ".join(order),"-->","Invalid year")
    order = input().strip().split()
def extract_time(m):
    dim = [31,28,31,30,31,30,31,31,30,31,30,31]
    x = m.copy()
    x[2:] = [int(j) for j in x[2:]]
    total_days = (x[4]*366)+(x[3]*dim[x[3]-1])+x[2]
    return total_days
res = sorted(res,key=lambda x:(extract_time(x),x[0]))
for e in res:
    print(str(e[0])+": delivered on","/".join(e[2:]))