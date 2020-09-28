def perm(n:int, s:str, op:int, cl:int, A):
	if op + cl == n * 2:
		A.append(s)
	if op < n :
		perm (n, s + '(', op + 1, cl, A)
	if op - cl > 0:
		perm (n, s + ')', op, cl + 1, A)
	return A

def BalancedParentheses(N):
	A = perm(N, s='', op=0, cl=0, A=[])
	A = ' '.join(A)
	return A
