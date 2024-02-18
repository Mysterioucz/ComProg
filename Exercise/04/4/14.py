# t = input()
# n = t.count("ABC")
# print(n) 
#โกงไประบบไม่ให้ใช้ 55555
t = input()
c = 0
for i in range(len(t)):
    if t[i:i+3]=="ABC":
        c +=1
print(c)