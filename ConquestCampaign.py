def ConquestCampaign(N:int, M:int, L:int, battalion:list):
	day = 0
	k = 1
	Land =  [[0] * M for i in range(N)]
	Land_1 = [[0] * M for i in range(N)]
	for d in range(0, len(battalion), 2):
		Land_1[battalion[d]-1][battalion[d + 1]-1] = 1
	while k > 0:
		for n in range(N):
			for m in range(M):
				Land[n][m] = Land_1[n][m]
		day += 1
		k = 0
		for n in range(N):
			for m in range(M):
				if k == 0 and Land [n][m] == 0:
					k = 1
				if Land[n][m] == 1 and m > 0 and n > 0 and n < (N - 1) and m < (M - 1):
					Land_1[n - 1][m] = 1
					Land_1[n + 1][m] = 1
					Land_1[n][m + 1] = 1
					Land_1[n][m - 1] = 1
				if m == 0 and Land[n][m] == 1 and n > 0 and n < (N - 1):
					Land_1[n - 1][m] = 1
					Land_1[n + 1][m] = 1
					Land_1[n][m + 1] = 1
				if n == 0 and Land[n][m] == 1 and m > 0 and m < (M - 1):
					Land_1[n + 1][m] = 1
					Land_1[n][m + 1] = 1
					Land_1[n][m - 1] = 1
				if n == (N - 1) and Land[n][m] == 1 and m > 0 and m < (M - 1):
					Land_1[n - 1][m] = 1
					Land_1[n][m + 1] = 1
					Land_1[n][m - 1] = 1
				if m == (M - 1) and Land[n][m] == 1 and n > 0 and n < (N - 1):
					Land_1[n - 1][m] = 1
					Land_1[n + 1][m] = 1
					Land_1[n][m - 1] = 1
				if Land[0][0] == 1:
					Land_1[0][1] = 1
					Land_1[1][0] = 1
				if Land[N - 1][0] == 1:
					Land_1[N - 2][0] = 1
					Land_1[N - 1][1] = 1
				if Land[0][M - 1] == 1:
					Land_1[0][M - 2] = 1
					Land_1[1][M - 1] = 1
				if Land[N - 1][M - 1] == 1:
					Land_1[N - 2][M - 1] = 1
					Land_1[N - 1][M - 2] = 1
	return day
