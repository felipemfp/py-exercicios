# Implementar:
# - um servidor que publique um objeto distribuído e este evoque a função tribonacci.
# - um cliente que use o objeto distribuído para calcular a sequência de Tribonacci.

import Pyro4

class Tribonnaci(object):
    def get_tribonnaci(self, n):
        if type(n) is not int or n < 1:
            raise TypeError
        t = [1, 1, 2]
        if n < 4:
            return  t[:n]
        for i in range(3, n):
            t.append(sum(t[-3:]))
        return t


daemon = Pyro4.Daemon(port = 8888)
uri = daemon.register(Tribonnaci, "Tribonnaci")
print("URI:", uri)
daemon.requestLoop()

# URI: PYRO:Tribonnaci@localhost:8888