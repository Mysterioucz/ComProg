sec = input().strip()
file = open("data.txt",'r')
score_total = 0
c = 0
for line in file:
    line = line.split(':')
    st_sec = line[2]
    st_score = float(line[3])
    if st_sec == sec:
        score_total += st_score
        c += 1
if c!=0 :
    print(score_total/c)
else:
    print('Not Found')