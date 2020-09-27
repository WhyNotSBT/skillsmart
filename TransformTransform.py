def S(A:list):
	B = []
	j = 0
	for i in A:
		while True:
			k = i + j
			B.append(max(A[j:k + 1]))
			if j < (len(A) - i - 1):
				j += 1
			else:
				break
	return B

def TransformTransform(A:list, N:int):
	if (sum(S(S(A))) % 2) == 0:
		return True
	return False
