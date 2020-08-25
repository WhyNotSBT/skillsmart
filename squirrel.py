def squirrel(N):
	factorial = 1
	if N == 0:
		return 1
	else:
		for i in range(1, N + 1):
			factorial = factorial * i
	F = str(factorial)
	return int(F[0])



