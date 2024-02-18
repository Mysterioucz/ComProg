def reverse(d):
 # d เป็น dict ที่มี value ไม่ซ ้ำกนั
 # คืน dict ใหม่ที่เก็บ key,value ที่ค่ำเป็น value,key ของ d ที่ได ้รับ
    res = {}
    for k in d:
        res[d[k]] = k
    return res
def keys(d, v):
 # คืนลิสต์ที่เก็บค่ำของ keys ใน d (เรียงยังไงก็ได ้) ที่มีค่ำ value เท่ำกับ v
    res = []
    for k in d:
        if d[k] == v:
            res.append(k)
    return res
exec(input().strip()) # ตอ้ งมคี ำสั่งนี้ ตรงนี้ตอนสง่ ให้Grader ตรวจ
