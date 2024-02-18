n = int(input())
data = {}
def reverse(d):
 # d เป็น dict ที่มี value ไม่ซ ้ำกนั
 # คืน dict ใหม่ที่เก็บ key,value ที่ค่ำเป็น value,key ของ d ที่ได ้รับ
    res = {}
    for k in d:
        res[d[k]] = k
    return res
for i in range(n):
    x = input().split()
    data[x[0]] = x[1]
datar = reverse(data)
n1 = int(input())
for i in range(n1):
    f = False
    out = input().strip()
    if out in data:
        print(data[out])
    elif out in datar:
        print(datar[out])
    else:
        print('Not found')