# def preob(matrix:list):
#     n = len(matrix)
#     c=0
#     for i in range(n):
#         if 2*abs(matrix[i][i])>=sum([abs(p) for p in matrix[i]]):
#             if 2 * abs(matrix[i][i]) > sum([abs(p) for p in matrix[i]]):
#                 c= c+1
#             continue
#         for j in range(i+1,n):
#             if 2*abs(matrix[j][i])>=sum([abs(p) for p in matrix[j]]):
#                 if 2 * abs(matrix[j][i]) > sum([abs(p) for p in matrix[j]]):
#                     c = c + 1
#                 break
#         else:break
#         matrix[i],matrix[j] = matrix[j],matrix[i]
#     else:
#         if c>0:
#             return matrix
#         else:
#             return False
#     return False

def gaus(n:list,p: list, eps:float,):
    trans = diag_matrix(n,len(n))
    if (trans[1] == False):
        print("Матрицу нельзя привести к диагональному преобладанию")
        return False
    matr = trans[0]
    b=[]
    if len(n)==1: matr = matr[0]
    for i in matr:
        b.append(p[n.index(i)])

    l = len(n)
    x = b.copy()
    x_p = b.copy()
    count_int=1
    for i in range(l):

        x[i] = b[i] / matr[i][i] - sum([(matr[i][j] / matr[i][i]) * x[j] for j in range(i )]) - sum(
            [(matr[i][j] / matr[i][i]) * x[j] for j in range(i+1,l)])

    while (condit(x,x_p,eps)[0]==False):
        count_int += 1
        x_p = x.copy()
        for i in range(l):
            x[i] = b[i] / matr[i][i] - sum([(matr[i][j] / matr[i][i]) * x[j] for j in range(i)]) - sum(
                [(matr[i][j] / matr[i][i]) * x[j] for j in range(i + 1, l)])

    return [x,max([sum(matr[i][j] for j in range(l)) for i in range(l)]),count_int, condit(x,x_p,eps)[1]]

def condit(x:list,y:list,eps:float):
    re = []
    for i in range (len(x)):
        if abs(x[i]-y[i])<=eps:
            re.append(abs(x[i]-y[i]))
            continue
        break
    else: return [True,re]
    return [False,re]

def diag_matrix(mat:list, deg:int,c=0):
    n=len(mat)
    if n==1:
        if 2*abs(mat[0][-1]) >= sum([abs(j) for j in mat[0]]):
            if 2 * abs(mat[0][-1]) > sum([abs(j) for j in mat[0]]):c=c+1

            return [[mat[0]],c]
        else: return [False,c]
    if (n == deg):
        ex = 0
        for i in range(n):
            if 2*abs(mat[i][0])>= sum([abs(j) for j in mat[i]]):
                c=0
                if 2 * abs(mat[i][0]) >sum([abs(j) for j in mat[i]]):c=1
                rem = mat[0:i]+mat[i+1:n]
                res,c = diag_matrix(rem,deg,c)
                if (res == False or c==0):continue
                ex = [mat[i]]+res
                break
        else: return [[[]],False]
        return [ex,True]
    else:
        k = deg-n
        for i in range(n):
            if 2 * abs(mat[i][k]) >= sum([abs(j) for j in mat[i]]):
                if 2 * abs(mat[i][k]) > sum([abs(j) for j in mat[i]]):
                    c=c+1
                rem = mat[0:i] + mat[i + 1:n]
                res,c = diag_matrix(rem,deg,c)
                if res == False:continue
                ex = [mat[i]]+res
                break
        else: return [False,c]
        return [ex,c]



