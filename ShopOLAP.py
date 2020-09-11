def ShopOLAP(N:int, string:list):
	d = []
	Data = {}
	product = []
	p = []
	value = []
	v = []
	new_string = []
	sort = {}
	s = []
	for i in string:
		z = i.split()
		d.append(z)
	for i in d:
		if i[0] in Data:
			Data[i[0]] += int(i[1])
		else:
			Data[i[0]] = int(i[1])
	for key in Data:
		value.append(Data[key])
		product.append(key) 
	for z in range(len(value)):
		index_max = value.index(max(value))
		v.append(value.pop(index_max))
		p.append(product.pop(index_max))
	t = 1
	i = 0
	while i < len(v):
		while ((i + t) < len(v)) and (v[i + t] == v[i]):
			if p[i] not in s:
				s.append(p[i])
			s.append(p[i + t])
			t += 1
		if len(s) > 1:
			s = sorted(s)
			s = s[::-1]
			sort[v[i]] = s
			s = []
		i += t
		t = 1
	for j in range(len(v)):
		if v[j] in sort:
			new_string.append(sort[v[j]].pop() + " " + str(v[j]))
		else:
			new_string.append(p[j] + " " + str(v[j]))
	return new_string