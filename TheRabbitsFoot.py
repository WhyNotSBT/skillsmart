from math import sqrt
def TheRabbitsFoot(s:str, encode: bool):
	cod = ""
	matrix = []
	D = s.split()
	if encode:
		for i in D:
			cod += i
		N = len(cod)
		if (sqrt(N) % 1) > 0:
			columns = int((sqrt(N) // 1)) + 1
			lines = int(sqrt(N) // 1)
		else:
			columns = int(sqrt(N))
			lines = int(sqrt(N))
		if columns * lines < N:
			lines += 1
		for i in range(lines):
			if len(cod) >= columns:
				matrix.append(cod[:columns])
				cod = cod[columns:]
			else:
				matrix.append(cod)
		cod = ""
		for j in range(columns):
			for i in range(len(matrix)):
				if len(matrix[i]) > 0:
					cod += matrix[i][:1]
					matrix[i] = matrix[i][1:]
			if j < columns - 1:
				cod += " "
		return cod
	else:
		for i in range(len(D[0])):
			for j in range(len(D)):
				if len(D[j]) >= i:
					cod += D[j][i:i+1]
		return cod
