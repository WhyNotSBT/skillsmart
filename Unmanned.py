def Unmanned(L:int, N:int, track:list):
	time = 0
	i = 0
	for k in range(1, L+1):
		time += 1
		if i < N and k == track[i][0]:
			if (time//(track[i][1] + track[i][2])) * (track[i][1] + track[i][2]) + track[i][1] >= time:
				time += ((time // (track[i][1] + track[i][2])) * (track[i][1] + track[i][2])) + track[i][1] - time
				i += 1
	return time

