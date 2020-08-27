def PatternUnlock(N:int, hits:list):
	j = 0
	for p in range(N - 1):
		if (hits[p + 1] == 2) and (hits[p] == 9 or hits[p] == 7 or hits[p] == 4 or hits[p] == 6):
			j += 1.414213562373
		elif (hits[p] == 2) and (hits[p + 1] == 9 or hits[p + 1] == 7 or hits[p + 1] == 4 or hits[p + 1] == 6):
			j += 1.414213562373
		else:
			j += 1
		k = hits[p]
	j = "%.5f" % (j)
	j = j.replace(".", "")
	j = j.replace("0", "")
	return j