x = input('input ')
if x.isdigit():
    print('digit')
else:
    if x in "AEIOU":
        print('vowel');
    elif x.isupper():
        print('capital letter')