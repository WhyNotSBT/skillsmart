def hoar_sort(A:list):
	if len(A) <= 1:
		return
	barrier = A[0]
	Left = []
	Middle = []
	Right = []
	for i in range(len(A)):
		if A[i] > barrier:
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


def MaximumDiscount(N:int, price:list):
	discount = 0
	i = 2
	hoar_sort(price)
	while i <= N - 1:
		print(price[i])
		discount += price[i]
		i += 3
	return discount
