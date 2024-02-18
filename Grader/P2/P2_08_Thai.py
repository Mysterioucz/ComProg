def to_Thai(num):
    res = ""
    nums = int(num)
    if nums>=1000:
        res += dict_num[nums//1000]+" pun "
    if nums>=100:
        if (nums%1000)//100 == 0:
            pass
        else:
            res += dict_num[(nums%1000)//100] + " roi "
    if nums>=10:
        if (num%100)//10 == 2:
            res += "yi sip "
        elif (num%100)//10 == 1:
            res += "sip "
        elif (num%100)//10 == 0:
            pass
        else:
            res += dict_num[(nums%100)//10] + " sip "
    if nums>=10 and nums%10 == 1:
        res += "et"
    elif nums != 0 and nums%10 == 0:
        pass
    else:
        res += dict_num[nums%10] 
    return res.strip()
    
dict_num = {0:"soon",1:"neung",2:"song",3:"sam",4:"si",5:"ha",6:"hok",7:"chet",8:"paet",9:"kao"}
exec(input().strip())
# for i in range(10000):
#     print(to_Thai(i))