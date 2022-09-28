def primes(until):
	until = until ** 0.5
	until = int(until - (until % 10)) +1

	prime_n = []
	
	for i in range(2, until):
		print('1st:', i, is_prime, prime_n)
		is_prime = True
		for j in prime_n:
			print('2nd:', i, is_prime, prime_n)
			if is_prime:
				print('3rd', i, is_prime, prime_n)
				if not i % j:
					is_prime = False
			else:
				print('4th:', i, is_prime, prime_n)
				break
		if is_prime:
			prime_n.append(i)
	
	return prime_n

def add(number, added, soustava):
	number = number * 10 + added
	return number

def mk_numbers(digits, list, start):
	soustava = len(digits)
	for i in digits:
		index = start
		for j in range(i):
			for k in range(soustava -i):
				if j +1 == i and k +1 == soustava -i:
					break
				while index >= len(list):
					list.append(0)
				list[index] = add(list[index], i, soustava)
				index += 1
			index += i -j -2

def order(soustava):
	numbers = []
	digits = list(range(soustava))
	len_d = len(digits)

	mk_numbers(digits, numbers, 0)

	start = 0
	for i in digits:
		start += (soustava - i)
	start = start - 2 *soustava +1

	mk_numbers(digits[::-1], numbers, start)
	return numbers

#soustava = int(input('v jake soustave: '))
#numbers = order(soustava)
#prime_num = primes(max(numbers))
#print(*ordefr(soustava), '\n\n', *prime_num, '\n\n')

numbers = list(range(10))
prime_num = primes(max(numbers))
print(*numbers, '\n\n', *prime_num, '\n\n')

for i in numbers:
	check = True
	#print(i, check)
	for j in prime_num:
		#print('		', i, j, check)
		if 0 == i % j:
			check = False
			break
		elif j > i:
			break
		#print('		didnt')

	if check:
		print(i)