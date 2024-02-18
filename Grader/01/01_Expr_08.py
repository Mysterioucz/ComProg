def sqrt_n_times(x, n):
    x **= (1 / 2)**n
    return x

def cube_root(y):
    y = sqrt_n_times(y, 2)
    for i in range(1,6):# i (1,2,3,4,5)
        y *= sqrt_n_times(y, 2**i) #2 4 8 16 32

    return y

def main():
    q = float(input())
    print(cube_root(q))

exec(input())  # DON'T remove this line