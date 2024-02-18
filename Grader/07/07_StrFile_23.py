name,y = input().strip().split()
file = open(name,'r')
score = []
for line in file:
    if line.split()[0][:2] == y[-2:]:
        score.append(float(line.split()[1]))
file.close()
if score == []:
    print('No data')
else:
    print(min(score),max(score),sum(score)/len(score))