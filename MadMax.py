def hoar_sort(A:list):
	if len(A) <= 1:
		return
	barrier = A[0]
	Left = []
	Middle = []
	Right = []
	for i in range(len(A)):
		if A[i] < barrier:
			Left.append(A[i])
		elif A[i] == barrier:
			Middle.append(A[i])
		else:
			Right.append(A[i])
	hoar_sort(Left)
	hoar_sort(Right)
	k = 0
	for x in Left+Middle+Right:
		A[k] = x
		k += 1


def MadMax(N:int, Tele:list):
	hoar_sort(Tele)
	for i in range(N//4+1):
		Tele[N//2 + i],Tele[N -1 -i] = Tele[N -1 -i],Tele[N//2 + i]
	return Tele