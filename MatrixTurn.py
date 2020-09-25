def MatrixTurn(Matrix: list, M:int, N:int, T:int):
	A = []
	K = min(M,N)//2
	TurnMatrix = [[0] * N for i in range(M)]
	for i in range(len(Matrix)):
		Matrix[i] = list(Matrix[i])
	Matrix01 = Matrix[:]
	while len(Matrix01) > 0:
		A = A + Matrix01[0]
		Matrix01 = Matrix01[1:]
		Matrix01 = [list(i) for i in zip(*Matrix01)]
		Matrix01 = Matrix01[::-1]
	for i in range(K):
		Matrix01.append(A[:(M + N) * 2 - 4])
		A = A[(M + N) * 2 - 4:]
		M -= 2
		N -= 2
	for i in range(len(Matrix01)):
		Matrix01[i] = Matrix01[i][-T:] + Matrix01[i][:-T]
	for i in range(len(Matrix01)):
		for j in range(len(Matrix01[i])):
			A += Matrix01[i][j]
	i = k = s = 0
	c = 1
	M = len(TurnMatrix)
	N = len(TurnMatrix[0])
	while i < len(A):
		while k < (N - c) and i < len(A):
			TurnMatrix[s][k] = A[i]
			k += 1
			i += 1
		while s < (M - c) and i < len(A):
			TurnMatrix[s][k] = A[i]
			s += 1
			i += 1
		while k > (c - 1) and i < len(A):
			TurnMatrix[s][k] = A[i]
			k -= 1
			i += 1
		c += 1
		while s > (c - 1) and i < len(A):
			TurnMatrix[s][k] = A[i]
			s -= 1
			i += 1
	for i in range(len(TurnMatrix)):
		Matrix[i] = ''.join(TurnMatrix[i])

