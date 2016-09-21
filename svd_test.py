def grad(a, b, A, eps):
    Da = {}
    Db = {}
    for i in range(len(A)):
        Da[i] = 0
        for j in range(len(A[0])):
            Da[i] += 2 * (a[i] * b[j] - A[i][j]) * b[j]
        Da[i] = a[i] - Da[i] * eps 
    for j in range(len(A)):
        Db[j] = 0
        for i in range(len(A[0])):
            Db[j] += 2 * (a[i] * b[j] - A[i][j]) * a[i]
        Db[j] = b[j] - Db[j] * eps
    return Da, Db

def L(a, b, A):
    count = 0
    for i in range(0, len(A)):
        for j in range(0, len(A[0])):
            count += (a[i] * b[j] - A[i][j]) ** 2
    return count



if __name__ == "__main__":
    
    A = [[1, 3], [2, 7]]
    a = [0, 1]
    b = [3, 4]
    eps = 0.2
    l0 = 2
    l1 = 1
    l2 = 1000
    eps_marker = eps


    while (eps > 0) and (l1 != l0):
        eps /= 2
        l0 = 1000
        l1 = L(a, b, A)
        print('eps:', eps)
        while (l1 < l0):
            print('l:', l1, 'a:', a, 'b:', b)
            a, b = grad(a, b, A, eps)
            l0 = l1
            l1 = L(a, b, A)
        if (l0 < l2) and (l0 != 1000):
            l2 = l0
            eps_marker = eps




    #test
    import numpy as np
    a = [0.673082414511689, 1.5505513664063575]
    b = [1.3209155110944957, 4.505419254524138]

    print()
    print('A', np.array(A))
    print()
    print("A':", np.array([[x * y for y in b] for x in a]))

    print(l2, eps_marker)



