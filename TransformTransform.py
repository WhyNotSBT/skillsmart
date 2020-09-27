def S(A:list):
	B = []
	for i in range(len(A)):
		for j in range(len(A) - i):
			k = i + j
			B.append(max(A[j:k + 1]))
	return B

def TransformTransform(A:list, N:int):
	if sum(S(S(A))) % 2 == 0:
		return True
	return False
