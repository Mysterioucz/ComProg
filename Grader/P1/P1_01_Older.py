a = input().replace(",","").split()
b = input().replace(",","").split()
m = ['January','February','March','April','May','June','July','August','September','October','November','December']
a[2] = int(a[2]);a[3] = int(a[3]);a[1]=m.index(a[1])
b[2] = int(b[2]);b[3] = int(b[3]);b[1]=m.index(b[1])
if a[3]>b[3]:
    print(b[0])
elif a[3]<b[3]:
    print(a[0])
else:
    if a[1]>b[1]:
        print(b[0])
    elif a[1]<b[1]:
        print(a[0])
    else:
        if a[2]>b[2]:
            print(b[0])
        elif a[2]<b[2]:
            print(a[0])
        else:
            print(a[0],b[0])