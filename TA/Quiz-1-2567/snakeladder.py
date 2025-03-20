def create_map(map_index,n,col):
    for i in range(n):
        for j in range(col):
            if i%2 == 0:
                map_index[i][j] = i*col + (j + 1)
            else:
                map_index[i][j] = (i + 1)*col - j

n = int(input())
map_index = [] # [[1,2,3,4],[5,6,7,8]]
# print(map_index)

snake_pos = [] ;ladder_pos = [] ;snake_dest = []; ladder_dest = []
for i in range(n-1, -1, -1): 
    map = input().split()
    if len(map_index) == 0:
        map_index = [[0 for a in range(len(map))] for b in range(n)]
        create_map(map_index,n,len(map))
    for j in range(len(map)):
        if "S" in map[j] :
            snake_pos.append(map_index[i][j])
            # print(map_index[i][j])
            snake_dest.append(int(map[j][1:]))
        elif "L" in map[j] :
            ladder_pos.append(map_index[i][j])
            ladder_dest.append(int(map[j][1:]))

# print(snake_pos, snake_dest)
# print(ladder_pos, ladder_dest)
move = [int(e) for e in input().split()]
cur_pos = 0;
for i in range(len(move)):
    cur_pos += move[i]
    
    if cur_pos in snake_pos:
        cur_pos = snake_dest[snake_pos.index(cur_pos)]
    elif cur_pos in ladder_pos:
        cur_pos = ladder_dest[ladder_pos.index(cur_pos)]
        
    if cur_pos >= len(map)*n:
        print("win", end = " ")
        break
    else:
        print(cur_pos, end = " ")