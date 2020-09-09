def TankRush( H1:int, W1:int, S1:str, H2:int, W2:int, S2:str):
	S1 = S1.split()
	for i in range(H1 - H2 + 1):
		find = ''
		for k in range(W1 - W2 + 1):
			for j in range(H2):
				find += S1[j + i][k:k + W2] + " "
		if S2 in find:
			return True
	return False
