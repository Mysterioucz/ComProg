n = int(input())
map = ['start']
for i in range(n):
    row  = input().split()
    if i % 2 != 0:
        row = row[::-1]
    map += row
# print(map)
pos = 0
i = 0
move = [int(e) for e in input().split()]
for i in range(len(move)):
    pos += move[i]
    if pos >= len(map) - 1:
        print("win")
        break
    if 'T' in map[pos] or 'S' in map[pos]:
        pos = int(map[pos][1:])
    if pos >= len(map) - 1:
        print("win")
        break
    elif pos != 0:
        print(pos, end = " ")