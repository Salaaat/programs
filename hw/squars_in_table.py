from random import randint

def mk_table(min, max):
	n = randint(min, max)
	m = randint(min, max)
	table = []

	for i in range(n):
		table.append([])
		for j in range(m):
			if randint(0, 1):
				table[i].append(True)
			else:
				table[i].append(False)

	return table

def find_sqr():
	min = 4
	max = 10
	table = mk_table(min, max)
	pot_sqrs = [[]]
	sqrs = [[[0,0],[0,0]]]

	for i in table:
		length = 0
		for j in i:
			if j:
				length += 1
			else:
				length = 0
			if len(sqrs) -1 < length:	#pot error
				sqrs.append([])
			if len(pot_sqrs) -1 < length:	#pot error
				pot_sqrs.append([])
			if not sqrs[length]:
	print(table, pot_sqrs)
find_sqr()