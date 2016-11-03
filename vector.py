def grad(a, b, A, eps):
	Da = {}
	Db = {}
	for i in range(len(A)):
		Da[i] = 0
		for j in range(len(A[0])):
			Da[i] += 2 * (a[i] * b[j] - A[i][j]) * b[j]
		Da[i] = a[i] - Da[i] * eps
	for j in range(len(A[0])):
		Db[j] = 0
		for i in range(len(A)):
			Db[j] += 2 * (a[i] * b[j] - A[i][j]) * a[i]
		Db[j] = b[j] - Db[j] * eps
	return Da, Db

def L(a, b, A):
	count = 0
	for i in range(0, len(A)):
		for j in range(0, len(A[0])):
			count += (a[i] * b[j] - A[i][j]) ** 2
	return count

def svd_by_vectors(a, b, A, eps):  
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

	l2, eps_marker, a, b = svd_by_vectors(a, b, A, eps)
	print()
	print('A', np.array(A))
	print()
	print("A':", np.array([[a[x] * b[y] for y in range(len(b))] for x in range(len(a))]))
	print()
	print('L:' + str(l2) + '\n' + 'eps:' + str(eps_marker))
	print('a:', a)
	print('b:', b)




if __name__ == "__main__":

	#test
	A = [[1, 3], [2, 7]]
	a = [0, 1]
	b = [3, 4]
	eps = 0.2

	test(a, b, A, eps)


