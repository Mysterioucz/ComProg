import math
def distance1(x1, y1, x2, y2):
 dis = math.sqrt((x1-x2)**2+(y1-y2)**2)
 return dis

def distance2(p1, p2):
 dis = math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
 return dis

def distance3(c1, c2):
 dis = distance2(c1,c2)
 overlap = False
 if c1[2]+c2[2] >= dis:
     overlap = True
 return dis,overlap

def perimeter(points):
 length = 0
 for i in range(len(points)-1):
     length += distance2(points[i],points[i+1])
 length += distance2(points[-1],points[0])
 return length
exec(input().strip()) # ตอ้ งมคี าสงั่ นี้ ตรงนี้ตอนสง่ ให้Grader ตรวจ