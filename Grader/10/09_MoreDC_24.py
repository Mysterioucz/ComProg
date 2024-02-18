animal = input().split(", ")
data,step = {},[]
while animal[0] != 'q':
    name,ani_type = animal[0],animal[1]
    if ani_type not in data:
        step.append(ani_type)
        data[ani_type] = [name]
    else:
        data[ani_type].append(name)
    animal = input().split(", ")
for k in step:
    print(k+':',", ".join(data[k]))