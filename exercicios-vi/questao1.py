# Implementar um módulo com uma função tribonacci(n) que retorne uma
# lista de n números de Tribonacci, aonde n é o parâmetro da função. Faça
# testes da função caso o módulo seja executado como principal.

def tribonnaci(n):
    """
    Return a list with n tribonacci numbers

    >>> t = [1, 1, 2]
    >>> t == tribonnaci(3)
    True
    """
    if type(n) is not int or n < 1:
        raise TypeError
    t = [1, 1, 2]
    if n < 4:
        return  t[:n]
    for i in range(3, n):
        t.append(sum(t[-3:]))
    return t


def __doctest():
    import doctest
    doctest.testmod()


if __name__ == "__main__":
    __doctest()