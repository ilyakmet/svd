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




A = [[1, 3], [2, 7]]
a = [0, 1]
b = [3, 4]
eps = 0.1

print(grad(a, b, A, eps))
print(L(a, b, A))



#todo
'''
l0 = 1000
l1 = L(a, b, A)
eps = 0.01

while (eps != 0) and (l1 != 0):
	eps /= 2
	a = [0, 1]
	b = [3, 4]
	l1 = L(a, b, A)
	print(eps)
	while (l1 != 0) and (l1 != l0) and (l1 < l0):
		print(l1, l0, a, b)
		a, b = grad(a, b, A, eps)
		l0 = l1
		l1 = L(a, b, A)

'''

