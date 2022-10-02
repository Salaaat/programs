def primes(until):
	until = int(until)
	primes = [2]
	
	for i in range(2, until):
		is_prime = True
		for j in primes:
			if is_prime:
				if not i % j:
					is_prime = False
			else:
				break
		if is_prime:
			primes.append(i)
	
	return primes

def m_p(a, primes):
	A = []
	i = 0

	if a:
		a = int(a)
		num = int(a)
		A.append(0)
		while primes[i] <= a ** 0.5:
			x = primes[i]
			if not num % x:
				num /= x
				A[i] += 1
			else: 
				A.append(0)
				i += 1
			if num in primes:
				j = 0
				while primes[j] != num:
					j += 1
				while len(A) - 1 != j:
					A.append(0)
				A[j] += 1
				break
			if num == 1:
				break
				
	return A
	
def count():
	prime = primes(input("nejvyssi cislo v uloze: "))

	while True:
		check = True
		a = input("a = ")
		b = input("b = ")
		n = input("n = ")
		d = input("D = ")

		print(prime)

		A = m_p(a, prime)
		B = m_p(b, prime)
		N = m_p(n, prime)
		D = m_p(d, prime)
		
		print(f"\n{A}\n{B}\n{N}\n{D}\n")
		
		while not(A and B and N and D):
			if A and B and not D:
				shorter = None
				longer = None
				if len(A) < len(B):
					shorter, longer = A, B
				else:
					shorter, longer = B, A
				for i in range(len(shorter)):
					D.append(min(shorter[i], longer[i]))
			elif A and B and not N:
				shorter = None
				longer = None
				if len(A) < len(B):
					shorter, longer = A, B
				else:
					shorter, longer = B, A
				for i in range(len(shorter)):
					N.append(max(shorter[i], longer[i]))
				for i in range(len(longer)):
					if i <= len(shorter):
						N.append(longer[i])
			elif (bool(A) != bool(B)) and D:
				pass
			elif (bool(A) != bool(B)) and N:
				pass
		names = ['a', 'b', 'n', 'd']
		numbers = [a, b, n, d]
		num_prm = [A, B, N, D]
		for i in range(4):
			small = numbers[i]
			big = num_prm[i]
			if not small:
				small = 1
				for j in range(len(big)):
					for k in range(big[j]):
						small *= prime[j]
				print(f'{names[i]} = {small}')
	print(2 * '\n')
	
count()