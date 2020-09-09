def LineAnalysis(string:str):
	line = string.split("*")
	line = line [1:-1]
	print(line)
	for i in range(len(line) - 1):
		if line[i] != line[i + 1]:
			return False
	return True
