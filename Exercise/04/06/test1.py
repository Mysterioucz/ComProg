data = input().split(", ")
bank = sorted([e.split("=") for e in data],key=lambda x:float(x[1]),reverse = True)
for e in bank:
    print(e[0])