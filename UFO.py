def UFO(N, data:list, octal:bool):
	data_0о = []
	data_0x = []
	if octal:
		for i in data:
			data_0о.append(int(str(i), 8))
	else:
		for i in data:
			data_0x.append(int(str(i), 16))
	if octal:
		return data_0о
	else:
		return data_0x