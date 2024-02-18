#idea รับ input เป็น str จากนนั้นนำมาต่อเรื่อยๆจนถึงตัวท้าย และ split ช่องว่าง
#ใช้ slice แยก X,Y เป็นอีกลิสนึง และทำแบบเดิมชิวๆ
p = input()
a = ''
while p!= 'Zig-Zag' and p!='Zag-Zig':
    a += " " + p
    p = input()
a = a.split()
x = a[:-1:2]
y = a[1::2]
for i in range(len(x)):
    x[i] = int(x[i])
    y[i] = int(y[i])
if p == "Zig-Zag":
    l = min(x[::2]+y[1::2])
    h = max(y[::2]+x[1::2])
    
elif p == "Zag-Zig":
    h = max(x[::2]+y[1::2])
    l = min(y[::2]+x[1::2])
print(l,h)

#Bad Solu แอบใช้ List
# p = input()
# a = ''
# while p!= 'Zig-Zag' and p!='Zag-Zig':
#     a += " " + p
#     p = input()
# a = list(map(int,a.split()))
# x = a[:-1:2]
# y = a[1::2]
# if p == "Zig-Zag":
#     l = min(x[::2]+y[1::2])
#     h = max(y[::2]+x[1::2])
    
# elif p == "Zag-Zig":
#     h = max(x[::2]+y[1::2])
#     l = min(y[::2]+x[1::2])
# print(l,h)
#---------------------------------------
#คิดทีละบรรทัด
# h,l = [int(e) for e in input().split()]
# i,j=h,l
# a = input().split() #[str[0], str[1]]
# c = 2
# while a != ['Zig-Zag'] and a != ['Zag-Zig']:
#     if c%2 ==0:
#         h = min(h,int(a[1]))
#         l = max(l,int(a[0]))
#         i = max(i,int(a[1]))
#         j = min(j,int(a[0]))
#     else:
#         h = min(h,int(a[0]))
#         l = max(l,int(a[1]))
#         i = max(i,int(a[0]))
#         j = min(j,int(a[1]))
#     a = input().split()
#     c += 1
# if a == ['Zig-Zag']:
#     print(h,l)

# elif a == ['Zag-Zig']:
#     print(j,i)