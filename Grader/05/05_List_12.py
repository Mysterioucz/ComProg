name = ['Robert','William','James','John','Margaret','Edward','Sarah','Andrew','Anthony','Deborah' ]
nick = ['Dick','Bill','Jim','Jack','Peggy','Ed','Sally','Andy','Tony','Debbie' ]
n = int(input())
for i in range(n):
    x = input()
    if x in name:
        print(nick[name.index(x)])
    elif x in nick:
        print(name[nick.index(x)])
    else:
        print("Not found")