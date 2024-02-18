def print_triangle(h):
    b = 2*h-1
    print("."*(h-1)+"*")
    for i in range(2,h):
        print("."*(h-i)+"*"+ "."*(2*i-3) +"*")
    print("*"*b)    
exec(input())