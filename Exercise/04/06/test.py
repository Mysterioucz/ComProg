st,test = [int(e) for e in input().split()]
data = []
error = []
for i in range(st):
    x = input().split()
    if len(x[1:]) == test:
        data.append([x[0],sum([float(num) for num in x[1:]])])
    else:
        error.append(x[0])
    data.sort(key=lambda item:(item[1],item[0]),reverse=True)
if len(error) != 0:
    print("Invalid data:")
    for e in error:
        print(e)
else:
    for e in data:
        print(e[0],e[1])
