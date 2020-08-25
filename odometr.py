def odometr(Oksana:list):
	distance = 0
	time = 0
	for t in range(1, len(Oksana), 2):
		distance = distance + (Oksana[t] - time) * Oksana[t - 1]
		time = Oksana[t]
	return distance

