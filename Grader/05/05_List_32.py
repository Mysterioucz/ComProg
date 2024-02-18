n = int(input())
raw,time,qtime,ticket = [],[],[],[]
for i in range(n):
    raw.append(input().split())
num = int(raw[0][1])
e,ec,eo = 0,0,0
for i in range(len(raw)):
 if raw[i][0] == 'new':
     print('ticket',num)
     ticket.append(num)
     time.append(int(raw[i][1]))
     num +=1
     e += 1
 elif raw[i][0] == 'next':
     print('call',ticket[ec])
     eo=ec
     ec += 1
 elif raw[i][0] == 'order':
     print('qtime',ticket[eo],int(raw[i][1])-time[eo])
     qtime.append(int(raw[i][1])-time[eo])
 elif raw[i][0] == 'avg_qtime':
     print('avg_qtime',round(sum(qtime)/len(qtime),4))