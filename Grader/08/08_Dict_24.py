def text2keys( text ):
    res=''
    for e in text.lower():
        if e.isalpha():
            for k in convertr:
                if e in k:
                    res += convertr[k]*(k.index(e)+1)+' '
        elif e == ' ':
            res += '0 '
    return res.strip()
def keys2text( keys ):
    res=''
    data = keys.split()
    for e in data: 
        if e.isnumeric() and e != '0':
            for k in convert:
                if k in e:
                    res += convert[e[0]][len(e)-1]
        elif e == '0':
            res += ' '
    return res.strip()    
def reverse(x):
    res={}
    for k in x:
        res[x[k]]=k
    return res
convert = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
convertr = reverse(convert)
exec(input().strip())
