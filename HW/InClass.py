import math

def create_sq_mat():
    raw_data = [int(num) for num in input().split()]
    mat_size = int(math.sqrt(len(raw_data)))
    res = [raw_data[i:i+mat_size] for i in range(0,len(raw_data),mat_size)]
    return [data for data in res if len(data)==mat_size] # [1,2,3,4] => [[1,2],[3,4]]
#[0,1,2,3,4,5,6,7,8] => [[0,1,2],[3,4,5],[6,7,8]] // 0 - 3 (0,1,2),3-6 (3,4,5),6-9 (6,7,8)

def even_list(d):
    return [num for num in d if num%2 == 0] # [(data),(Loop),(Condition)]

def count_even_num(d):#[1,2,3,4] => [false,true,false,true] = [0,1,0,1] => sum([0,1,0,1]) = 2
    return sum([num%2==0 for num in d]) # True = 1, False = 0
exec(input().strip()) # DON'T remove this 