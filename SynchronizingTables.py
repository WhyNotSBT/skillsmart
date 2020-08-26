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


def SynchronizingTables(N, ids:list, salary:list):
	Buffer = [0] * N
	ID = ids[:]
	k = 0
	hoar_sort(ID)
	hoar_sort(salary)
	d = {ID[a]: salary[a] for a in range(N)}
	for i in ids:
		Buffer[k] = d[i]
		k += 1
	salary = Buffer[:]
	return salary
