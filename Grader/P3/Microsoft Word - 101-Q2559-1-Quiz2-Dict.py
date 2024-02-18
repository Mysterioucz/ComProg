def add_to(key,M_name):
    for k in key:
        if k in act:
            act[k].append(M_name)
        else:
            act[k] = [M_name]


n = int(input())
act = {}
for i in range(n):
    data = input().split(", ")
    add_to(data[1:],data[0])
actor_name = input().strip().split(", ")
for name in actor_name:
    if name in act:
        print(name,"->",", ".join(act[name]))
    else:
        print(name,"->","Not found")