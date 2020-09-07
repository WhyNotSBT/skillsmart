def who_bigger(s1:str, s2:str):
	if len(s1) == len (s2):
		n = 0
		while n < len(s1):
			if s1[n] == s2[n]:
				n += 1
			elif s1[n] > s2[n]:
				return True
			else:
				return False
	else:
		return True


def BigMinus(s1:str, s2:str):
	difference = ""
	diff = 0
	i = 0
	if (len(s1) >= len(s2)) and who_bigger(s1, s2):
		num1 = s1[::-1]
		num2 = s2[::-1]
	else:
		num1 = s2[::-1]
		num2 = s1[::-1]
	while i < len(num2):
		diff = diff + int(num1[i:i + 1]) - int(num2[i: i + 1])
		if diff < 0:
			difference = str(10 + diff) + difference
			diff = -1
		else:
			difference = str(diff) + difference
			diff = 0
		i+=1
	while i < len(num1):
		diff = int(num1[i:i + 1]) + diff
		if diff < 0:
			difference = str(10 + diff) + difference
			diff = -1
		else:
			difference = str(diff) + difference
			diff = 0
		i += 1
	while int(difference[:1]) == 0:
		difference = difference[1:]
	return difference


