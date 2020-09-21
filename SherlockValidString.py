def SherlockValidString(s:str):
	Flag = True
	D = {}
	for i in s:
		if i in D:
			D[i] += 1
		else:
			D[i] = 1
	print(D)
	Val = sorted(list(D.values()))
	print(Val)
	if (Val[0] != Val[-1]) and len(Val) > 2:
		if Val[0] == 1:
			Val = Val[1:]
			if Val[0] == Val[-1]:
				return True
		Val = sorted(list(D.values()))
		print(Val)
		if Val[0] == (Val[-1] - 1):
			for i in range(2,len(Val) - 1):
				if Val[0] != Val[-i]:
					return False
			return True
	if len(Val) == 2:
		if Val[0] == Val[-1]:
			return True
		elif Val[0] == 1:
			return True
		elif Val[0] == (Val[-1] - 1):
			return True
		else:
			return False
	return False
