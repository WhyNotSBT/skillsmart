def perm(n:int, s:str, op:int, cl:int):
	global A
	if op + cl == n * 2:
		A.append(s)
	if op < n :
		perm (n, s + '(', op + 1, cl)
	if op - cl > 0:
		perm (n, s + ')', op, cl + 1)


def BalancedParentheses(N):
	global A
	perm(N, s='', op=0, cl=0)
	A = ' '.join(A)
	return(A)

A = []
