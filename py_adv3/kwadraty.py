def square(n):
    '''
    Zwraca kwadrat liczby b

    >>> square(0)
    0
    >>> square(1)
    1
    >>> square(2)
    4
    >>> square(3)
    9
    >>> square()
    Traceback (most recent call last):
    TypeError: square() missing 1 required positional argument: 'n'

    :param n (int): Numer podnoszony do kwadratu
    :return: int jako rezultat
    '''
    return n ** 2



if __name__ == '__main__':
    import doctest
    doctest.testmod()