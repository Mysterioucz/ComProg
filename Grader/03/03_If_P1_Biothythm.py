import math
bd, bm, by, d, m, y = [int(e) for e in input().split()]
y -= 543
days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
def dayyear(d,m,y):
    if y%400==0 or (y%4 == 0 and y%100 != 0 ):
        days[2] = 29
    s = (sum(days[:m])+d)
    return s
def dayyearleft(d,m,y):
    if y%400==0 or (y%4 == 0 and y%100 != 0 ):
        days[2] = 29
    s = sum(days[:])-(sum(days[:m])+d)
    return s
td = (y-by-1)*365 + (dayyear(d,m,y)) + (dayyearleft(bd,bm,by))
if y==by:
    td -= 1
phy ='{:.2f}'.format(math.sin((2*math.pi*td)/23)) #format จะทำการ round ให้โดยบังคับให้มีทศนิยม 2 ตน เช่น 0.9 = 0.90 และเปลี่ยนประเภทข้อมูลเป็น Str
em = '{:.2f}'.format(math.sin((2*math.pi*td)/28))
inte = '{:.2f}'.format(math.sin((2*math.pi*td)/33))
# print(type(inte))
print(td,phy,em,inte)