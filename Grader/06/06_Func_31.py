mname = ["Jan", "Feb","Mar","Apr",
 "May","Jun","Jul","Aug",
 "Sep","Oct","Nov","Dec"]
dm = [31,28,31,30,31,30,31,31,30,31,30,31]
def read_date():
    x = input().split()
    x[1] = mname.index(x[1]) +1
    x[0],x[2] = int(x[0]),int(x[2])
    return x

def zodiac(d,m): 
    if d >= 22 and m==3 or d <=21 and m==4 : z1 = "Aries"
    elif d >= 22 and m==4 or d<=21 and m==5 : z1 = "Taurus"
    elif d >= 22 and m==5 or d<=21 and m==6 : z1 = "Gemini"
    elif d >= 22 and m==6 or d<=21 and m==7 : z1 = "Cancer"
    elif d >= 22 and m==7 or d<=21 and m==8 : z1 = "Leo"
    elif d >= 22 and m==8 or d<=21 and m==9 : z1 = "Virgo"
    elif d >= 22 and m==9 or d<=21 and m==10 : z1 = "Libra"
    elif d >= 22 and m==10 or d <=21 and m==11 : z1 = "Scorpio"
    elif d >= 22 and m==11 or d <=21 and m==12 : z1 = "Sagittarius"
    elif d >= 22 and m==12 or d <=20 and m==1 : z1 = "Capricorn"
    elif d >= 21 and m==1 or d<=20 and m==2 : z1 = "Aquarius"
    elif d >= 21 and m==2 or d<=21 and m==3 : z1 = "Pisces"
    return z1

def days_in_feb(y): # คืนจำนวนวันของเดือนกุมภาพันธ์ในปี y
    if y % 400 == 0 or y % 100 != 0 and y%4 == 0 :
        return 29
    return 28

def days_in_month(m,y): 
    if m == 2:
        return days_in_feb(y)
    else:
        return dm[m-1]
        
def days_in_between(d1,m1,y1,d2,m2,y2):
    days = 0
    if m1 < 12 : days += 31
    if m1 < 11 : days += 30
    if m1 < 10 : days += 31
    if m1 < 9 : days += 30
    if m1 < 8 : days += 31
    if m1 < 7 : days += 31
    if m1 < 6 : days += 30
    if m1 < 5 : days += 31
    if m1 < 4 : days += 30
    if m1 < 3 : days += 31
    if m1 < 2 : days += days_in_feb(y1)
    if m2 > 1 : days += 31
    if m2 > 2 : days += days_in_feb(y2)
    if m2 > 3 : days += 31
    if m2 > 4 : days += 30
    if m2 > 5 : days += 31
    if m2 > 6 : days += 30
    if m2 > 7 : days += 31
    if m2 > 8 : days += 31
    if m2 > 9 : days += 30
    if m2 > 10 : days += 31
    if m2 > 11 : days += 30
    days += (days_in_month(m1,y1) - d1 + 1) + int((y2 - y1 - 1)*365.25) + (d2 - 1)
    return days
def main() :
 d1,m1,y1 = read_date()
 d2,m2,y2 = read_date()
 print(zodiac(d1,m1),zodiac(d2,m2))
 print(days_in_between(d1,m1,y1,d2,m2,y2))
exec(input().strip()) # ต้องมีบรรทัดนี้เมื่อส่งไป grader