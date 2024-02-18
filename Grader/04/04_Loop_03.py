key = input()
ans = input()
c = 0
if len(key) == len(ans):
    for i in range(len(key)):
        if key[i]==ans[i]:
            c += 1
    print(c)
else:
    print("Incomplete answer")           
