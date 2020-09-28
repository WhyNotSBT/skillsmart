def BalancedParentheses(N:int, s='', op=0, cl=0, A=[]):
	if op + cl == N * 2:
		A.append(s)
	if op < N :
		BalancedParentheses(N, s + '(', op + 1, cl, A)
	if op - cl > 0:
		BalancedParentheses(N, s + ')', op, cl + 1, A)
	A = ' '.join(A)
	return A
