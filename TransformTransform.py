def Transform(A:list):
	B = []
	for i in A:
		for j in range(len(A) - i - 1):
			k = i + j
			B.append(max(A[j:k + 1]))
	return B

def TransformTransform(A:list, N:int):
	if sum(Transform(Transform(A))) % 2 == 0:
		return True
	return False
