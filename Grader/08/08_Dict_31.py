def total(pocket):
    total = 0
    for k in pocket:
        total += k*pocket[k]
    return total
    
def take(pocket, money_in):
    for k in money_in:
        if k in pocket:
            pocket[k] += money_in[k]
        else:
            pocket[k] = money_in[k]
    

def pay(pocket, amt):
    if total(pocket) < amt:
        pocket = {}
        return {}
    else:
        out = {}
        pocket_k = sorted(list(pocket.keys()),reverse = True)
        for k in pocket_k:
            if amt >= k*pocket[k]:
                amt -= k*pocket[k]
                out[k] = pocket[k]
            elif k<amt:
                out[k] = amt//k
                amt -= out[k]*k
        for k in out:
            pocket[k] -= out[k]
        return out
        # while money != 0:
        #     for k in pocket_k:
        #         if money//k > 0:
        #             out[k] = 0
        #     out_k = sorted(list(out.key()),reverse = True)
        #     for e in out_k:
        #         while money//e > 0 and out[e]+1 <= pocket[e]:
        #             money -= e
        #             out[e] += 1
        #     b_out = out.copy()
        #     for e in out_k:
        #         if out[e] == 0:
        #                 b_out.pop(e)
        #     out = b_out.copy()
        #     out_k = list(out)
        # for k in out_k:
        #     if out[k]>pocket[k]:
        #         check = False
        #         return{}
        #     else:
        #         check = True
        # if check:
        #     for k in out_k:
        #         pocket[k] -= out[k]
        # return out

exec(input().strip()) # ตอ้ งมคี ำสั่งนี้ ตรงนี้ตอนสง่ ให้Grader ตรวจ