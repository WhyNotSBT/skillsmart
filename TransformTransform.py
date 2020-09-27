def Transform(A:list):
	B = []
	for i in A:
		if (len(A) - i - 1) > 0: 
			for j in range(0,len(A) - i - 1):
				k = i + j
				B.append(max(A[j:k]))
		else:
			B.append(max(A[0:i]))
	return B

def TransformTransform(A:list, N:int):
	if sum(Transform(Transform(A))) % 2 == 0:
		return True
	return False
