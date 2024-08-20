"""Donut"""
import math
def main():
    """Donut"""
    a = abs(int(input()))
    b = abs(int(input()))
    c = abs(int(input()))
    d = abs(int(input()))
    if not a and not b and not c and not d:
        print("0", "0")
    elif d < b:
        print(d * a, d)
    elif not c:
        print(d * a, d)
    elif not d:
        print(d, c)
    else:
        setdonut = b + c
        cost = b * a
        mindonut = d // setdonut
        total = mindonut * cost
        alldonut = (mindonut * setdonut) + (d-(mindonut * setdonut))
        print(total, alldonut)

main()
