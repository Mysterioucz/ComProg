# First Try
# def day_of_year(d, m, y):
#     y -= 543
#     y1 = [0,31,59,90,120,151,181,212,243,273,304,334]
#     y2 = [0,31,60,91,121,152,182,213,244,274,305,335]
#     if y%4 ==0:
#         if y%100 ==0:
#             if y%400 ==0:
#                 s=y2[m-1]+d
#             else:
#                 s=y1[m-1]+d
#         else:
#             s=y2[m-1]+d
#     else:
#         s=y1[m-1]+d
#     return s
# exec(input())
def day_of_year(d, m, y):
    y -= 543
    days=[0,31,28,31,30,31,30,31,31,30,31,30,31]
    if y%400 == 0 or (y%4==0 and y%100 != 0):
        days[2] = 29
    s = sum(days[:m])+d
    return s
exec(input())