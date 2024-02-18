import math
a = input()
b_list = a.split(",") #['7','','0']
a_list = str(a.split(",")) #"['7','','0']"
a_list = (a_list.replace("''", "0").strip("[]").replace("'", "").replace(",", "")).split() #"7  0  0"
dec_sum = int(a_list[1] + a_list[2]) - int(a_list[1])
b = int(len(b_list[2]) * "9" + len(b_list[1]) * "0")
div = math.gcd(dec_sum, b)
print((b // div) * int(a_list[0]) + dec_sum // div, "/", b // div)  
# ใช้หารปัดเศษเพราะถ้าเป็นเลขจำนวนมากๆมันจะบึ้ม
# print(int((b//div)*int(a_list[0])+dec_sum//div)/int(b//div))
