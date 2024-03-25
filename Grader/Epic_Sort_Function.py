def pai_sort(e):# [i,j,k]
    main = [str(i) for i in range(2,10)]+["X","J","Q","K","A","H","D","S","C"]
    return main.index(e)
def function(lis):
    return (pai_sort(lis[1]),lis[0])
card_list = [e.split("|") for e in input().split()]
print(sorted(card_list,key=lambda x:[pai_sort(x[1]),x[0]])) #Same result Wiht line 8
print(sorted(card_list,key=function))
