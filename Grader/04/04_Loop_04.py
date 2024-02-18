n = list(input())
for i in range(len(n)) :
    if n[i]=='(':
        n[i] = '['
    elif n[i]=='[':
        n[i] = '('
    elif n[i]==')':
        n[i] = ']'
    elif n[i]==']':
        n[i] = ')'
n = ''.join(n) #แปลง n จาก list มาเป็น str
print(n)