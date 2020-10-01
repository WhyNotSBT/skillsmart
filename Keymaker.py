def Keymaker(k:int):
	Door = [1] * k
	if k == 0:
		return '1'
	for n in range(2 ,k + 1):
		for i in range(n-1,k,n):
			if Door[i] == 0:
				Door[i] += 1
			elif Door[i] == 1:
				Door[i] -= 1
	for i in range(k):
		Door[i] = str(Door[i])
	Door = ''.join(Door)
	return Door
