def show():
    for e in fruit:
        print(" ".join(e))
    return
def get(some):
    fruit_name = [e[0] for e in fruit]
    if some in fruit_name:
        for e in fruit:
            if e[0] == some:
                print(" ".join(e))
                break
    else:
        print(some,"not found")
    return
def avg(m):
    total = 0
    for e in fruit:
        total += float(e[int(m)])
    print(round(total/len(fruit),4))
    return
def s_key(elem): #Key ในการ sort 
    return float(elem[int(method[1])])
def sort():# sort โดยการใช้ tuple ที่มี key1,key2
    res = sorted(fruit,key=lambda x:(s_key(x),x[0]))
    return res
def max():
    res = sorted(fruit,key=lambda x:(-float(x[int(method[1])]),x[0]))
    print(res[0][0],res[0][int(method[1])])
n = int(input())
fruit=[]
for i in range(n):
    fruit.append(input().split())
method = input().split()
if "show" in method:
    show()
elif "get" in method:
    get(method[1])
elif "avg" in method:
    avg(int(method[1]))
elif "max" in method:
    max()
elif "sort" in method:
    for e in sort():
        print(e[0],end = " ")