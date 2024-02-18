n = int(input())
data = {}
for i in range(n):
    song_genre,duration = input().split(', ')[-2:]
    minute,sec = [int(e) for e in duration.split(':')]
    if song_genre in data:
        data[song_genre][0] += minute
        data[song_genre][1] += sec
    else:
        data[song_genre] = [minute,sec]
for k in data:
    minute = data[k][0]
    sec = data[k][1]
    data[k][0] = minute + sec//60
    data[k][1] = sec%60
res = sorted(data,key=lambda x:(data[x][0],data[x][1]),reverse=True)
for e in res[:3]:
    print(e,'-->',str(data[e][0])+":"+str(data[e][1]).zfill(2))
        
    