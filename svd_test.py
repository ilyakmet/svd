def grad(a, b, A, eps):
	w0, w1, v0, v1 = 0, 0, 0, 0
	for i in range(0, 2):
		for j in range(0, 2):
			if not i:
				w0 += 2 * (a[i] * b[j] - A[i][j]) * b[j]
				v0 += 2 * (b[i] * a[j] - A[j][i]) * a[j]
			else:
				w1 += 2 * (a[i] * b[j] - A[i][j]) * b[j]
				v1 += 2 * (b[i] * a[j] - A[j][i]) * a[j]
	res = [[w0, w1], [v0, v1]]
	return [a[x] - res[0][x] * eps for x in range(0, 2)], [b[x] - res[1][x] * eps for x in range(0, 2)]

def L(a, b, A):
	count = 0
	for i in range(0, 2):
		for j in range(0, 2):
			count += (a[i] * b[j] - A[i][j]) ** 2
	return count



if __name__ == "__main__":
	
	A = [[1, 3], [2, 7]]
	a = [0, 1]
	b = [3, 4]
	eps = 0.1
	l1 = 1
	l0 = 2
	l2 = 1000

	while (eps > 0) and (l1 != l0):
		eps /= 2
		l0 = 1000
		l1 = L(a, b, A)
		print('eps:', eps)
		while (l1 < l0):
			print('l1:', l1, 'l0:', l0, 'a:', a, 'b:', b)
			a, b = grad(a, b, A, eps)
			l0 = l1
			l1 = L(a, b, A)
		if (l0 < l2) and (l0 != 1000):
			l2 = l0
			eps_marker = eps
		#print('l1:', l1, 'l0:', l0, 'a:', a, 'b:', b)




	#test
	import numpy as np
	a = [0.673082414511689, 1.5505513664063575]
	b = [1.3209155110944957, 4.505419254524138]

	print()
	print('A', np.array(A))
	print()
	print("A':", np.array([[x * y for y in b] for x in a]))

	print(l2, eps_marker)






