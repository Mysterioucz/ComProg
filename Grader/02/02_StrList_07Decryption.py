k = ["A","B","C","D","E","F","G","H","I","J","K"]
a = input()
a = list(a)
b = a[3] + a[10] + a[17] + a[24] + a[31]
c = a[7] + a[12] + a[17] + a[22] + a[27]
b = int(b)
c = int(c)
result = b + c +10000
m = result%10000
j = list(str(m))
j = j[0] + j[1] + j[2]
m = list(map(int, str(m)))
n = m[0] + m[1] + m[2]
n = n%10
final = k[n]
print(j + final )

