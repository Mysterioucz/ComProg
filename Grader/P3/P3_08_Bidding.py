n = int(input().strip())
prod,user,winner = {},{},{}
c = 0
for _ in range(n):
    auction = input().split()
    if auction[0] == 'B':
        if auction[2] not in prod:
            prod[auction[2]] = [[auction[1],int(auction[3])]]
            winner[auction[2]] = []
        elif any(auction[1] in x for x in prod[auction[2]]):
            for i in range(len(prod[auction[2]])):
                if (prod[auction[2]][i][0] == auction[1]):
                    prod[auction[2]].pop(i)
                    prod[auction[2]].append([auction[1],int(auction[3])])
        else:
            prod[auction[2]].append([auction[1],int(auction[3])])
        if auction[1] not in user:
            user[auction[1]] = [0]
    elif auction[0] == 'W':
        if auction[2] in prod:
            if any(auction[1] in x for x in prod[auction[2]]):
                for i in range(len(prod[auction[2]])):
                    if prod[auction[2]][i][0] == auction[1]:
                        prod[auction[2]].pop(i)
                        break
for k in prod:
    for v in prod[k]:
        if len(winner[k]) == 0:
            winner[k] = v
        elif winner[k][1]<v[1]:
            winner[k] = v
for k,v in winner.items():
    if len(v)>0:
        if user[v[0]] == [0]:
            user[v[0]] = [v[1],k]
        else:
            user[v[0]][0] += v[1]
            user[v[0]].append(k)
for u in sorted(user):
    price,name = user[u][0],user[u][1:]
    if price==0:
        print(u+':','$'+str(price))
    else:
        print(u+':','$'+str(price),"->"," ".join(sorted(name)))
# print(user)
