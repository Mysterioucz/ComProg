mode = input()
c = 1
r =''
if mode == 'str2RLE':
    d = input()
    for i in range(len(d)):
        if i != len(d)-1 :
            if  d[i] == d[i+1]:
                c += 1
            else:
                r += str(d[i])+" "+str(c)+" "
                c = 1
        else:
            r += str(d[i])+" "+str(c)
    print(r)
        
elif mode == 'RLE2str':
    d = input()
    d = d.split()
    for i in range(0,len(d),2):
        r += d[i]*int(d[i+1])
    print(r)
else:
    print("Error")