def grad(a, b, A, eps):
    Da = [[0 for x in range(len(a[0]))] for y in range(len(a))]
    for i in range(0, len(a)):
        for j in range(0, len(a[0])):
            res_2 = 0
            for n in range(0, len(b)):
                res = 0
                for k in range(0, len(b[0])):
                    res += a[i][k] * b[n][k]
                res = 2 * (res - A[i][n]) * b[n][j]
                res_2 += res
            Da[i][j] = a[i][j] - res_2 * eps

    Db = [[0 for x in range(len(b[0]))] for y in range(len(b))]
    for i in range(0, len(b)):
        for j in range(0, len(b[0])):
            res_2 = 0
            for n in range(0, len(a)):
                res = 0
                for k in range(0, len(a[0])):
                    res += b[i][k] * a[n][k]
                res = 2 * (res - A[n][i]) * a[n][j]
                res_2 += res
            Db[i][j] = b[i][j] - res_2 * eps

    return Da, Db

def L(a, b, A):
    count = 0
    for i in range(0, len(A)):
        for j in range(0, len(A[0])):
            count_2 = 0
            for n in range(len(a[0])):
                count_2 += a[i][n] * b[j][n]
            count += (count_2 - A[i][j]) ** 2
    return count

def svd_by_matrix(a, b, A, eps):  
        l0 = 2
        l1 = 1
        l2 = 1000
        a_l2, b_l2 = None, None
        eps_marker = eps
        while (eps > 0) and (l1 != l0):
            eps /= 2
            l0 = 1000
            l1 = L(a, b, A)
            print('eps:', eps)
            while (l1 < l0):
                print('l:', l1, 'a:', a, 'b:', b)
                a_old, b_old = a, b
                l0 = l1
                a, b = grad(a, b, A, eps)
                l1 = L(a, b, A)
            if (l0 < l2) and (l0 != 1000):
                l2 = l0
                eps_marker = eps
                a_l2, b_l2 = a_old, b_old
        return l2, eps_marker, a_l2, b_l2

def test(a, b, A, eps):
    import numpy as np

    l2, eps_marker, a, b = svd_by_matrix(a, b, A, eps)
    print()
    print('A', np.array(A))
    print()
    
    A_new = [[0 for x in range(len(A[0]))] for y in range(len(A))]
    for i in range(0, len(A)):
        for j in range(0, len(A[0])):
            count_2 = 0
            for n in range(len(a[0])):
                count_2 += a[i][n] * b[j][n]
            A_new[i][j] = count_2

    print("A':", np.array(A_new))
    print()
    print('L:' + str(l2) + '\n' + 'eps:' + str(eps_marker))
    print('a:', a)
    print('b:', b)




if __name__ == "__main__":

    #test
    A = 
    a = 
    b = 
    eps = 0.2

    test(a, b, A, eps)


