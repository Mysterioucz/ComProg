def readfile(name):
    file = open(name,"r")
    res= {}
    for line in file:
        key,value=line.strip().split(',')
        res[key]=value
    file.close()
    return res
n_course = input().strip()
n_teacher = input().strip()
n_database = input().strip()
course,teacher=readfile(n_course),readfile(n_teacher)
data = open(n_database,'r')
for line in data:
    c_num,t_num = line.strip().split(',')
    if c_num in course and t_num in teacher:
        course_name = course[c_num]
        teach = teacher[t_num]
        print(str(course_name)+','+str(teach))
    else:
        print("record error")
