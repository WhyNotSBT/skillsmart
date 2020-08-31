def WordSearch(Len:int,s:str,subs:str):
	i = 0
	Index = []
	Check_Word = []
	A = s.split()
	N = len(A) - 1
	flag = 0
	for i in range(N//2 +1):
		A[i],A[N-i] = A[N-i],A[i]
	while len(A) >= 0:
		if flag == 0:
			word = A.pop()
		else:
			word = word1
		while len(word) >= Len:
			Index.append(word[:Len])
			word = word[Len:]
		if len(A) > 0:
			word1 = A.pop()
			flag = 1
		else:
			Index.append(word)
			break
		while (len(word) + 1 + len(word1)) <= Len:
			word = (word + " " + word1)
			if len(A) > 0:
				word1 = A.pop()
				flag = 1
			else:
				Index.append(word)
				break
		Index.append(word)
	Check_Word = [0] * (len(Index))
	for s in range(len(Index)):
		In_Line = Index[s].split()
		for k in In_Line:
			if subs == k:
				Check_Word[s] = 1		
	return Check_Word

