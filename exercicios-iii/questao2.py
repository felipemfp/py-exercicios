# Implementar o gerador de números primos como uma expressão (dica: use
# o módulo itertools)

from itertools import count
from questao1 import is_prime

primes = (x for x in count() if is_prime(x))


if __name__ == "__main__":
	for x in range(10):
		print(next(primes))


# 2
# 3
# 5
# 7
# 11
# 13
# 17
# 19
# 23
# 29