# Implementar:
# - um servidor que publique um objeto distribuído e este evoque a função tribonacci.
# - um cliente que use o objeto distribuído para calcular a sequência de Tribonacci.

import Pyro4.core

URI = "PYRO:Tribonnaci@localhost:8888"
proxy = Pyro4.Proxy(URI)

if __name__ == "__main__":
    for x in range(10):
        print("{:02} => {}".format(x + 1, proxy.get_tribonnaci(x + 1)))


# 01 => [1]
# 02 => [1, 1]
# 03 => [1, 1, 2]
# 04 => [1, 1, 2, 4]
# 05 => [1, 1, 2, 4, 7]
# 06 => [1, 1, 2, 4, 7, 13]
# 07 => [1, 1, 2, 4, 7, 13, 24]
# 08 => [1, 1, 2, 4, 7, 13, 24, 44]
# 09 => [1, 1, 2, 4, 7, 13, 24, 44, 81]
# 10 => [1, 1, 2, 4, 7, 13, 24, 44, 81, 149]