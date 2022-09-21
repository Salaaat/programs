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
		while i < len(primes):
			x = primes[i]
			if not a % x:
				a /= x
				A[i] += 1
			else: 
				i += 1
				A.append(0)
	return A
	
def count():
	prime = primes(input("nejvyssi cislo v uloze: "))
	
	while True:
		check = True
		a = input("a = ")
		b = input("b = ")
		d = input("D = ")
		n = input("n = ")
	
		A = m_p(a, prime)
		B = m_p(b, prime)
		D = m_p(d, prime)
		N = m_p(n, prime)
		
		print(f"\n{A}\n{B}\n{D}\n{N}\n")
		
		while not(A and B and D and N):
			if A and B and not N:
				index = 0
				for i in range(len(A)):
					if A[i] <= B[i]:
						pass
					index += 1
			elif A and B and not D:
				pass
			elif (bool(A) != bool(B)) and (D or N):
				pass

count()