class piggybank:
    def __init__(self):
        self.coins = {}
    def add(self, v, n):
        v = float(v)
        total_coins = sum([v for v in self.coins.values()])
        if total_coins + n <=100:
            if v not in self.coins:
                self.coins[v] = n
            else:
                self.coins[v] += n
            return True
        return False
    def __float__(self):
        return float(sum([self.coins[k]*k for k in self.coins]))
    def __str__(self):
        res = ""
        for k in sorted(self.coins):
            res += str(k) + ":"+ str(self.coins[k])+", "
        return "{"+res[:-2]+"}"
cmd1 = input().split(';')
cmd2 = input().split(';')
p1 = piggybank(); p2 = piggybank()
for c in cmd1: eval(c)
for c in cmd2: eval(c)