raw_vote = input().strip()
data = []
while not raw_vote.isnumeric():
    data.append(raw_vote.split())
    raw_vote = input().strip()
def total_vote():
    d_vote = {}
    for e in data:
        if e[1] not in d_vote:
            d_vote[e[1]] = int(e[2])
        else:
            d_vote[e[1]] += int(e[2])
    return(sorted(d_vote,key=lambda x:d_vote[x])[::-1][:3])
def vote():
    d_vote,voter={},{}
    for e in data:
        if (e[1] not in d_vote):
            voter[e[1]] = [e[0]]
            d_vote[e[1]] = 1
        elif (e[0] not in voter[e[1]]):
            voter[e[1]].append(e[0])
            d_vote[e[1]] += 1
    return (sorted(d_vote,key=lambda x:d_vote[x])[::-1][:3])
def kami():
    d_vote = {}
    bnk_name = []
    for e in data:
        if e[0] not in d_vote:
            d_vote[e[0]] = {e[1]:int(e[2])}
        elif e[1] not in d_vote[e[0]]:
            d_vote[e[0]][e[1]] = int(e[2])
        else:
            d_vote[e[0]][e[1]] += int(e[2])
        if e[1] not in bnk_name:
            bnk_name.append(e[1])
    res = {}
    for k,v in d_vote.items():
        kami_ochi = (sorted(v,key=lambda x:(-v[x],x),reverse=True))[-1]
        # print(k,kami_ochi)
        if kami_ochi not in res:
            res[kami_ochi] = 1
        else:
            res[kami_ochi] += 1
    for e in bnk_name:
        if e not in res:
            res[e] = 0
    return (sorted(res,key=lambda x:res[x]))[::-1][:3]
if raw_vote == '1':
    print(", ".join(total_vote()))
elif raw_vote == '2':
    print(", ".join(vote()))
elif raw_vote == '3':
    print(", ".join(kami()))