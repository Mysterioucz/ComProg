def grade_mcq(sol,ans):
    c = 0
    if len(sol)==len(ans):
        for i in range(len(sol)):
            if sol[i]==ans[i]:
                c += 1
    else:
        c = -1
    return c
exec(input())