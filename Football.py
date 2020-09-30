def Football(F:list, N:int):
	F_sort = sorted(F)
	if F == F_sort:
		return False
	A = []
	for i in range(N):
		if F[i] != F_sort[i]:
			A.append(i)
	if len(A) == 2:
		F[A[0]],F[A[1]] = F[A[1]],F[A[0]]
		if F == F_sort:
			return True
		else:
			return False
	if A[0] == 0:
		F[A[0]:A[-1] + 1] = F[A[-1]:: - 1]
	else:
		F[A[0]:A[-1] + 1] = F[A[-1]:A[0] - 1: - 1]
	if F == F_sort:
		return True
	return False
