n = int(input().strip())
point= {}
seq = []
def step(x):
    return seq.index(x)
for i in range(n):
    st_id,score = input().split()
    faculty = st_id[-2:]
    if faculty in point:
        point[faculty][0] += int(score)
        point[faculty][1] += 1
    else:
        seq.append(faculty)
        point[faculty] = [int(score),1]
avg_score = [[point[k][0]/point[k][1],k] for k in point]
max_avg = max(avg_score)[0]
top_faculty = [e[1] for e in avg_score if e[0] == max_avg ]
top_faculty.sort(key=step)
for e in top_faculty:
    print(e)
