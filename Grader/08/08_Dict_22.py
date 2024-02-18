n = int(input())
ice,sale = {},{}
for i in range(n):
    icecream = input().split()
    ice[icecream[0]] = icecream[1]
for k in ice:
    sale[k] = 0
n1 = int(input())
kaiook = False
for i in range(n1):
    prod = input().split()
    if prod[0] in ice:
        sale[prod[0]] += float(ice[prod[0]])*int(prod[1])
        kaiook = True
top = max(sale.values())
topsale = []
for k in sale:
    if sale[k] == top:
        topsale.append(k)
topsale.sort()
topsale = ", ".join(topsale)
if kaiook:
    print('Total ice cream sales:',sum(sale.values()))
    print('Top sales:',topsale)
else:
    print('No ice cream sales')