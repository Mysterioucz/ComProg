n = int(input())
winner = set()
loser = set()
for i in range(n):
    data = input().split()
    winner.add(data[0])
    loser.add(data[1])
print(sorted(winner-loser))