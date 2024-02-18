def str2hms(hms_str):
    # คนื จ ำนวนชั่วโมง นำทีและวนิ ำที ที่ดึงมำจำกสตริง hms
    # เชน่ str2hms("10:03:29") ได้ 10,3,29
    t = hms_str.split(":")
    return int(t[0]), int(t[1]), int(t[2])


def hms2str(h, m, s):
    # คืนสตริงในรูปแบบ HH:MM:SS ที่น ำจ ำนวนชั่วโมง นำที และวินำทีมำจำก h,m และ s
    # เชน่ hms2str(10,3,29) ได้ "10:03:29"
    return ("0" + str(h))[-2:] + ":" + ("0" + str(m))[-2:] + ":" + ("0" + str(s))[-2:]


def to_sec(h, m, s):
    sec = h * 3600 + m * 60 + s
    return sec


def to_hms(s):
    h = s // 3600
    m = s // 60 - h * 60
    s = s % 60
    return h, m, s


def diff(h1, m1, s1, h2, m2, s2):
    sum = abs((h1 * 3600 + m1 * 60 + s1) - (h2 * 3600 + m2 * 60 + s2))
    dh = sum // 3600
    dm = sum // 60 - dh * 60
    ds = sum % 60
    return dh, dm, ds


def main():
    hms_start = input()
    hms_end = input()
    start = list(
        map(int, hms_start.split(":"))
    )  # แบ่ง str จากinputแล้วแปลงเป็นจำนวนเต็มแล้วสร้างเป็นlist
    end = list(map(int, hms_end.split(":")))
    sum = abs(
        (start[0] * 3600 + start[1] * 60 + start[2])
        - (end[0] * 3600 + end[1] * 60 + end[2])
    )
    dh = sum // 3600
    dm = sum // 60 - dh * 60
    ds = sum % 60
    return print(
        ("0" + str(dh))[-2:] + ":" + ("0" + str(dm))[-2:] + ":" + ("0" + str(ds))[-2:]
    )  # ที่ใส้ [-2:] เพราะว่าในเคสที่เวลาในแต่ละหลักเป็น 2 หน่วย เช่น 10:20:35 เวลา +"0" ไปจะเป็น 010:020:035 เลยต้องsliceให้เหลือแค่ตัวที่ -2 ถึง -1


exec(input())  # DON'T remove this line
