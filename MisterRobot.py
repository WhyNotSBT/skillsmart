def MisterRobot(N:int, data:list):
	j = 0
	i = 1
	Unsort_data = data[:]
	data = [0]*N
	for c in range(1,N + 1):
		data[c - 1] = c
	while Unsort_data != data:
		Unsort_data1 = Unsort_data[:]
		if (Unsort_data[-i] < Unsort_data[-i - 1]) or (Unsort_data[-i] < Unsort_data[-i - 2]):
			while Unsort_data[-i] < Unsort_data[-i - 2] or Unsort_data[-i] < Unsort_data[-i - 1]:
				Unsort_data[-i - 2], Unsort_data[-i - 1], Unsort_data[-i] = Unsort_data[-i], Unsort_data[-i - 2], Unsort_data[-i - 1]
				j = 0
		if i < N - 2:
			i += 1
		else:
			i = 1
		if Unsort_data1 == Unsort_data:
			j += 1
		if j == N:
			return False
	return True
