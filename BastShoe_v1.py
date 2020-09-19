line = ''
change = []
rechange = []
ID = []


def BastShoe(command:str):
	global line, change, rechange, ID
	if command[:2] == '1 ':
		line += command[2:]
		if ID and ID[-1] == 4:
			change = [command]
			rechange = []
		else:
			change.append(command)
		ID.append(1)
	if command[:2] == '2 ':
		N = int(command[2:])
		if N < len(line):
			if ID and ID[-1] == 4:
				change = ['2 ' + line[ -N :]]
				rechange = []
			else:
				change.append('2 ' + line[ -N :])
			line = line[: -N ]
		else:
			if ID and ID[-1] == 4:
				change = ['2 ' + line]
				rechange = []
			else:
				change.append('2 ' + line)
			line = ''
		ID.append(2)
	if command[:2] == '3 ':
		N = int(command[2:])
		try:
			Elem = line[N]
			return Elem
		except IndexError:
			return ''
	if change and command == '4':
		last_change = change.pop()
		if last_change[:2] == '1 ':
			line = line[: -len(last_change) + 2]
			rechange.append(last_change)
		elif last_change[:2] == '2 ':
			line += last_change[2:]
			rechange.append(last_change)
		ID.append(4)
	if rechange and command == '5':
		last_rechange = rechange.pop()
		if last_rechange[:2] == '1 ':
			line += last_rechange[2:]
			change.append(last_rechange)
		elif last_rechange[:2] == '2 ':
			line = line[:-len(last_rechange) + 2]
			change.append(last_rechange)
	return line