score = {"R":1,"Y":2,"G":3,"W":4,"B":5,"P":6,"K":7}
amount = {"R":6,"Y":1,"G":1,"W":1,"B":1,"P":1,"K":1}
play = input().strip()
p_score = [0,0]

while play[1] != "K":
    p_num = int(play[0])-1
    for ch in play[1:]:
        if ch != "X":
            p_score[p_num] += score[ch]
    play = input().strip()
p_num = int(play[0])-1
p_score[p_num] += score[play[1]]
print(p_score[0],p_score[1])
if p_score[0]>p_score[1]:
    print("Player 1 wins")
elif p_score[0]<p_score[1]:
    print("Player 2 wins")
else:
    print("Tie")
        