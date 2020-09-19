def add_str(command):
	Shoe = open('Shoe.txt','a').write(command[2:])
	try:
		add = open('Change.txt','r').read()
		add = command + '\n' + add
		Change = open('Change.txt','w').write(add)
	except FileNotFoundError:
		Change = open('Change.txt','w').write(command + '\n')
	command_id = open('command_id.txt','r').read()
	if command_id and command_id[-1] == '4':
		Change = open('Change.txt','w').write(command + '\n')
		ReChange = open('ReChange.txt','w').write('')
	command_id = open('command_id.txt','a').write('1')


def del_str(command):
	N = int(command[2:])
	de = open('Shoe.txt','r').read()
	if N < len(de):
		try:
			add = open('Change.txt','r').read()
			add = '2 ' + de[ -N : ] + '\n' + add
			Change = open('Change.txt','w').write(add)
		except FileNotFoundError:
			Change = open('Change.txt','w').write('2 ' + de[ -N :])
		command_id = open('command_id.txt','r').read()
		if command_id and command_id[-1] == '4':
			Change = open('Change.txt','w').write('2 ' + de[ -N : ] + '\n')
			ReChange = open('ReChange.txt','w').write('')
		command_id = open('command_id.txt','a').write('2')
		de = de[: -N ]
		Shoe = open('Shoe.txt','w').write(de)
	else:
		de ='2 ' + de + '\n'
		Change = open('Change.txt','w').write(de)
		Shoe = open('Shoe.txt','w').write('')
		command_id = open('command_id.txt','r').read()
		if command_id and command_id[-1] == '4':
			Change = open('Change.txt','w').write(de)
			ReChange = open('ReChange.txt','w').write('')
		command_id = open('command_id.txt','a').write('2')


def Undo():
	back = open('Change.txt','r').readline()
	if back[:2] == '1 ':
		de = open('Shoe.txt','r').read()
		de = de[: -len(back) + 3]
		Shoe = open('Shoe.txt','w').write(de)
		try:
			add = open('ReChange.txt','r').read()
			add = back + add
			ReChange = open('ReChange.txt','w').write(add)
		except FileNotFoundError:
			ReChange = open('ReChange.txt','w').write(back) 
		Change_line = open('Change.txt','r').read()
		Change = open('Change.txt','w').write(Change_line[len(back):])
	elif back[:2] == '2 ':
		de = open('Shoe.txt','r').read()
		de = de + back[2:-1]
		Shoe = open('Shoe.txt','w').write(de)
		try:
			add = open('ReChange.txt','r').read()
			add = back + add
			ReChange = open('ReChange.txt','w').write(add)
		except FileNotFoundError:
			ReChange = open('ReChange.txt','w').write(back)
		Change_line = open('Change.txt','r').read()
		Change = open('Change.txt','w').write(Change_line[len(back):])


def Redo():
	back = open('ReChange.txt','r').readline()
	if back[:2] == '1 ':
		Shoe = open('Shoe.txt','a').write(back[2:-1])
		ReChange_line = open('ReChange.txt','r').read()
		ReChange = open('ReChange.txt','w').write(ReChange_line[len(back):])
	elif back[:2] == '2 ':
		de = open('Shoe.txt','r').read()
		Shoe = open('Shoe.txt','w').write(de[:- len(back) + 3])
		ReChange_line = open('ReChange.txt','r').read()
		ReChange = open('ReChange.txt','w').write(ReChange_line[len(back):])
	Change_line = open('Change.txt','r').read()
	Change = open('Change.txt','w').write(back + Change_line)


def BastShoe(command:str):
	command_id = open('command_id.txt','a').write('')
	if command[:2] == '1 ':
		add_str(command)
	elif command[:2] == '2 ':
		del_str(command)
	elif command[:2] == '3 ':
		In = open('Shoe.txt','r').read()
		try:
			In = In[int(command[2:])]
			return In
		except IndexError:
			return ''
	elif command == '4':
		Undo()
		command_id = open('command_id.txt','a').write('4')
	elif command == '5':
		Redo()
	line = open('Shoe.txt','r').read()
	return line
	