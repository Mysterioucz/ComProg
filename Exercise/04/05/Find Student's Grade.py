st_id = input().strip()
file = open("score.txt",'r')
data = {}
for line in file:
    data[line.split()[0]] = line.split()[1]
file.close()
while st_id != "end":
    if st_id in data:
        print(data[st_id])
    else:
        print('Not Found')
    st_id = input().strip()