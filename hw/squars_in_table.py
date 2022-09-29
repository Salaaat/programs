from random import randint

def mk_table(min, max):	#makes random table of Trues and Falses
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

def find_sqr(min, max):	#findes the biggest square of Trues in random table of booleans
	#min = int(input('Minimum size of table: '))
	#max = int(input('Maximum size of table: '))
	table = mk_table(min, max)
	pot_sqrs = []	#index = length of one side; pot_sqrs[index] = list of coordinates of top left corners; i, j = table[i][j] (coordinates in table)
	sqrs = [[0,0]]	#index = length of one side; i, j = table[i][j] (coordinates of top left corners)

	for i in range(len(table)):
		row = table[i]
		length = 0
		print(row)

		for j in range(len(row)):
			cell = row[j]
			print(cell)

			if cell:
				length += 1
				while (len(sqrs) -1) < length:
					sqrs.append([])
				while (len(pot_sqrs) -1) < length:
					pot_sqrs.append([])
				
				not_len = length
				while not_len:
					if not sqrs[not_len]:
						pot_sqrs[not_len].append([i, j -(not_len -1)])
					not_len -= 1
			else:
				length = 0

