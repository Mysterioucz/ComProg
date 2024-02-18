fn = input()
n = int(input())

########################
txt = ''
f = open(fn, 'r')

for line in f:
    line = line.strip()
    txt += line + '.'

f.close()
txt = txt.strip('.')
txt += '.'
########################
ruler = ''
for i in range(n//10) :
    ruler += '-'*9 + str(i+1) # เพิ่มรอบละ 9 ขีด ตามด้วยตัวเลข
if n%9 != 0 :
    ruler += '-'*( n - 10*(n//10) ) # เพิ่มที่เหลือ (ถ้ามี)
print(ruler)
########################
pt = 0 # index ของการเริ่มต้นเก็บลง op
d0 = txt.find('.')
ind_dot = [] # list เก็บ index ของจุด
ind_dot.append(d0)
#d1 = txt.find('.',d0+1) # dot next to d0
op = txt[pt:ind_dot[-1]] # output

while True:
    if ind_dot[-1] == len(txt)-1:
        ck = op.strip('.')
        c = True
        for e in ck:
            if e == '.':
                c = False
        if c == True:
            break
        else:
            if len(op.strip('.')) > n:
                op = txt[pt:ind_dot[-2]].strip('.')
                if len(op) != 0:
                    print(op)
                op = txt[ind_dot[-2]:ind_dot[-1]]
        break
    if len(op.strip('.')) > n: # เกินลิมิต
        # check ก่อนว่ามาคำเดียวป่าว
        if len(op.strip('.').split('.')) == 1:
            print(op.strip('.'))
            pt = d0 # reset pt
        # ถ้าไม่ได้มาคำเดียว ต้องตัดคำออกและต้องยอ้นกลับมาไบ่ที่ index ก่อนหน้า
        else:
            d0 = ind_dot[-2]
            ind_dot.remove(ind_dot[-1])
            op = txt[pt:d0]
            op = op.strip('.')
            print(op)
            pt = d0
    elif len(op.strip('.')) == n: # พอดีลิมิต
        print(op.strip('.'))
        pt = d0
    d0 = txt.find('.',d0+1)
    if d0 == -1:
        break
    else:
        ind_dot.append(d0)
    op = txt[pt:ind_dot[-1]]
print(op.strip('.'))