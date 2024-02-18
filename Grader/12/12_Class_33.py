class piggybank:
    def __init__(self):
        self.data = {}
        self.data[1] = 0
        self.data[2] = 0
        self.data[5] = 0
        self.data[10] = 0
    def add1(self, n):
        self.data[1] += n
    def add2(self, n):
        self.data[2] += n
    def add5(self, n):
        self.data[5] += n
    def add10(self, n):
        self.data[10] += n
    def __int__(self):
        return sum([self.data[k]*k for k in sorted(self.data)])
    def __lt__(self, rhs):
        return int(self)<int(rhs)
    def __str__(self):
        return "{"+"1"+":"+str(self.data[1])+", "+"2"+":"+str(self.data[2])+", "+"5"+":"+str(self.data[5])+", "+"10"+":"+str(self.data[10])+"}"
        # return str(self.data).replace(": ",":") Python 3.5.1 Dict มันไม่เรียง
cmd1 = input().split(';')
cmd2 = input().split(';')
p1 = piggybank(); p2 = piggybank()
for c in cmd1: eval(c)
for c in cmd2: eval(c)
