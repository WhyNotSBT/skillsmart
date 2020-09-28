def Football(F:list, N:int):
	F_sort = sorted(F)
	Not_sort = []
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
	F = F[:A[0]] + F[A[-1]:A[0] - 1:-1] + F[A[-1] + 1:]
	if F == F_sort:
		return True
	return False
