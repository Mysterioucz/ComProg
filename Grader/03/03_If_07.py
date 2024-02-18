n = input()
d = len(n)

if d<=3:
    print(n)
elif 3<d<=6:
    if 1<=int(n)/1000<10 :
        print(str(round(int(n)/1000,1))+"K")
    else:
        print(str(int(int(n)/1000+0.5))+"K")
elif 6<d<=9:
    if 1<=int(n)/1e6<10 :
        print(str(round(int(n)/1e6,1))+"M")
    else:
        print(str(int(int(n)/1e6+0.5))+"M")
else :
    if 1<=int(n)/1e9<10 :
        print(str(round(int(n)/1e9,1))+"B")
    else:
        print(str(int(int(n)/1e9+0.5))+"B")