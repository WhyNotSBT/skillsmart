def SherlockValidString(s:str):
	sum_value = 0
	D = {}
	for i in s:
		if i in D:
			D[i] += 1
		else:
			D[i] = 1
	for key in D:
		sum_value += D[key]
	if (sum_value % len(D) == 0) or ((sum_value - 1) % len(D) == 0):
		return True
	elif (1 in D.values()) and ((sum_value - 1) % (len(D) - 1) == 0):
		return True
	else:
		return False
