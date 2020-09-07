def MassVote(N,Vote):
	case_3 = "no winner"
	Max = 0
	Sum = 0
	Index = []
	for i in range(N):
		if Vote[i] > Max:
			Max = Vote[i]
		Sum += Vote[i]
	for i in range(N):
		if Vote[i] == Max:
			Index.append(i)
	if len(Index) > 1:
		return case_3
	Percent = (Max * 100) / Sum
	Percent = "{0:.3f}".format(Percent)
	if float(Percent) > 50:
		case_1 = "majority winner " + str(Index[0] + 1)
		return case_1
	else:
		case_2 = "minority winner " + str(Index[0] + 1)
		return case_2
