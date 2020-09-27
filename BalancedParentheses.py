def Recursive(N:int, A: list):
	if N == 0:
		return A
	else:
		N -= 1
		string = A[-1][:]
		for i in range(len(string)):
			if string[i] == ')':
				string = string[:i - 1] + string[i + 1:] + '()'
				A.append(string)
				break
		Recursive(N, A)


def BalancedParentheses(N:int):
	string = '(' * N + ')' * N
	A = [string]
	Recursive(N - 1, A)
	A = ' '.join(A)
	return(A)
