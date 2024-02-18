class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    def __str__(self):
        return "("+self.value+" "+self.suit+")"
    def getScore(self):
        v = self.value
        if v in "JQK":v=10
        elif v == "A":v=1
        return int(v)
    def sum(self, other):
        v1,v2 = self.getScore(),other.getScore()
        return (v1+v2)%10
    def __lt__(self, rhs):
        key = [str(e) for e in [3,4,5,6,7,8,9,10,"J","Q","K","A",2,"club","diamond","heart","spade"]]
        if key.index(self.value) == key.index(rhs.value):
            return key.index(self.suit)<key.index(rhs.suit)
        return key.index(self.value)<key.index(rhs.value)
n = int(input())
cards = []
for i in range(n):
 value, suit = input().split()
 cards.append(Card(value, suit))
for i in range(n):
 print(cards[i].getScore())
print("----------")
for i in range(n-1):
 print(Card.sum(cards[i], cards[i+1]))
print("----------")
cards.sort()
for i in range(n):
 print(cards[i])