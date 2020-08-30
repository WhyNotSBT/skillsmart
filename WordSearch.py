def WordSearch(Len:int,s:str,subs:str):
	i = 1
	Index = []
	Check_Word = []
	A = s.split()
	while i < len(A):
		line = A[i - 1]
		if len(line) > Len:
			line_0 = line[:Len]
			Index.append(line_0)
			line = line[Len:]
		while (len(line) + len(A[i]) + 1) <= Len:
			line = (line + " " + A[i])
			if i < len(A) - 1:
				i += 1
		Index.append(line)
		i += 1
	if (i - 1 == len(A)-1) and not A[-1] in Index[-1]:
		Index.append(A[-1])
	Check_Word = [0] * (len(Index))
	for s in range(len(Index)):
		In_Line = Index[s].split()
		for k in In_Line:
			if subs == k:
				Check_Word[s] = 1
	return Check_Word