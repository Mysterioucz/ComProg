class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    def __str__(self):
        return "("+str(self.value)+" "+str(self.suit)+")"
    def next1(self):
        v,s = self.value,self.suit
        key = [str(e) for e in [3,4,5,6,7,8,9,10,"J","Q","K","A",2,"club","diamond","heart","spade"]]
        if v == "2" and s=="spade":
            return Card(3,"club")
        elif s == "spade":
            return Card(key[key.index(v)+1],"club")
        return Card(v,key[key.index(s)+1])
    def next2(self):
        x = self.next1()
        self.value,self.suit = x.value,x.suit
n = int(input())
cards = []
for i in range(n):
 value, suit = input().split()
 cards.append(Card(value, suit))
for i in range(n):
 print(cards[i].next1())
print("----------")
for i in range(n):
 print(cards[i])
print("----------")
for i in range(n):
 cards[i].next2()
 cards[i].next2()
 print(cards[i])
