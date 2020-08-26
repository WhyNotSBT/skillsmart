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


def SynchronizingTables(n, Ids:list, Salary:list):
	A = [0] * n
	k = 0
	hoar_sort(Salary)
	d = {a: Salary[a - 1] for a in range(1,n+1)}
	for i in Ids:
		A[k] = d[i] 
		k += 1
	return A