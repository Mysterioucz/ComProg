def main():
    a,b,c,d = [int(input()) for _ in range(4)]
    total_donut = {"b": (d//(b+c))*b, "c": (d//(b+c))*c}
    if max(0,(d-(d//(b+c))*(b+c))) >= b:
        total_donut["b"] += b
        total_donut["c"] += c
    else:
        total_donut["b"] += max(0,(d-(d//(b+c))*(b+c)))
    print(total_donut["b"]*a,sum(total_donut.values()))
main()