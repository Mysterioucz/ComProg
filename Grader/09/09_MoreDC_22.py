def read_matrix():
    m = []
    nrows = int(input())
    for k in range(nrows):
        x = input().split()
        r = []
        for e in x:
            r.append( float(e) )
        m.append(r)
    return m
def mult_c(c, A):
    res = [[c*e for e in A[i]] for i in range(len(A))]
    return res
def mult(A, B):
    res = [[sum([A[i][j]*B[j][k] for j in range(len(A[0]))]) for k in range(len(B[0]))] for i in range(len(A))] #len(A) คือ แถว len(A[0]) len(B[0]) คือหลักของB โดยที่หลักของ A ต้อง  = แถวของB ถึงจะคูณกันได้
    return res
exec(input().strip())