# Implementar um gerador de números primos

def is_prime(number):
	"""
	Verify if number is prime
	"""
	
	if number < 2: return False
	elif number == 2: return True
	elif number % 2 == 0: return False
	else:
		for x in range(2, number):
			if number % x == 0:
				return False
		else:
			return True


def prime_numbers(min = 2, max = 0):
	"""
	Generator for primes
	"""
	
	if max > 0:		
		for n in range(min, max + 1):
			if is_prime(n):
				yield n
	else:
		n = min
		while True:
			if is_prime(n):
				yield n
			n += 1


if __name__ == "__main__":
	for x in prime_numbers(max = 20):
		print(x)
	
# 2
# 3
# 5
# 7
# 11
# 13
# 17
# 19