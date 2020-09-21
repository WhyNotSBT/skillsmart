perm_list = []
def perm(a, k=0):
	global perm_list
	if k == len(a):
		A = list(a)
		perm_list.append(A)
	else:
		for i in range(k, len(a)):
			a[k], a[i] = a[i] ,a[k]
			perm(a, k+1)
			a[k], a[i] = a[i], a[k]


def BiggerGreater(Input:str):
	A = []
	orig = list(Input)
	re_sorted = sorted(orig, reverse = True)
	if orig == re_sorted:
		return ''
	global perm_list
	perm(orig)
	for i in perm_list:
		if i > orig:
			A.append(i)
	last = ''.join(min(A))
	return last