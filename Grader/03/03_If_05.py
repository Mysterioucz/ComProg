n = int(input())
if n != 0:
    if n>0 :
        print("positive")
        if n%2 == 0:
            print("even")
        else :
            print("odd")
    else:
        print("negative")
        if n%2 == 0:
            print("even")
        else :
            print("odd")
else:
    print("zero")
    print("even")