w = input().strip()
sara = "aeiou"
if w[-1]=='s' or w[-1]=='x' or w[-2::]=='ch':
    print(w+'es')
elif (w[-2] not in sara )and w[-1] == 'y':
    print(w[:-1]+'ies')
else:
    print(w+'s')