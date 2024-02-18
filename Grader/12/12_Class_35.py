roman_num = {"I":1,"IV":4,"V":5,"IX":9,"X":10,"XL":40,"L":50,"XC":90,"C":100,"CD":400,"D":500,"CM":900 ,"M":1000}
class roman :
    def __init__(self, r):
        self.rom = r
        self.value = 0
        i = 0
        while (i < len(r)):
            s1 = roman_num[r[i]]
            if (i + 1 < len(r)):
                s2 = roman_num[r[i+1]]
                if (s1 >= s2):
                    self.value +=  s1
                    i += 1
                else:
                    self.value +=s2 - s1
                    i += 2
            else:
                self.value += s1
                i += 1
    def __lt__(self, rhs):
        return self.value < rhs.value
    def __str__(self):
        return self.rom
    def __int__(self):
        return self.value
    def __add__(self, rhs):
        values = self.value + rhs.value
        res = ""
        for k in sorted(roman_num,key=lambda x:roman_num[x],reverse=True):
            if values//roman_num[k] >=1:
                res += k*(values//roman_num[k])
                values = values-(roman_num[k]*(values//roman_num[k]))
        return roman(res)     
t, r1, r2 = input().split()
a = roman(r1); b = roman(r2)
if t == '1' : print(a < b)
elif t == '2' : print(int(a),int(b))
elif t == '3' : print(str(a),str(b))
elif t == '4' : print(int(a + b))
else : print(str(a + b))