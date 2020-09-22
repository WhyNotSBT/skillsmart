def TreeOfLife( H:int , W:int , N:int , tree:list):
	for i in range(H):
		tree[i] = tree[i].replace('+', '1')
		tree[i] = tree[i].replace('.', '0')
		tree[i] = list(tree[i])
	for i in tree:
		for j in range(W):
			i[j] = int(i[j])
	for year in range(N):
		for i in range(H):
			for j in range(W):
				tree[i][j] += 1
		if year % 2 != 0:
			for k in range(H):
				for l in range(W):
					if tree[k][l] >= 3:
						tree[k][l] = 0
						if (k - 1 > -1) and tree[k - 1][l] < 3:
							tree[k - 1][l] = 0
						if (k + 1 < H) and tree[k + 1][l] < 3:
							tree[k + 1][l] = 0
						if (l + 1 < W) and tree[k][l + 1] < 3:
							tree[k][l + 1] = 0
						if (l - 1 > -1) and tree[k][l - 1] < 3:
							tree[k][l - 1] = 0
	for i in tree:
		for j in range(W):
			if i[j] == 0:
				i[j] = '.'
			else:
				i[j] = '+'
	for i in range(H):
		tree[i] = ''.join(tree[i])
	return tree
