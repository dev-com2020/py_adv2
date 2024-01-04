import math
import time


def time_deco(fun):
    def wrapper(*args):
        result = fun(*args)
        print(time.perf_counter())
        return result

    return wrapper


@time_deco
def factorial(x, y):
    fact = math.factorial(x)
    time.sleep(2)
    fact2 = math.factorial(y)
    print(math.gcd(fact, fact2))


factorial(10000, 10)


def attrs(**kwargs):
    def deco(f):
        for k in kwargs:
            setattr(f, k, kwargs[k])
        return f
    return deco


@attrs(version=3.11, author="Tomek")
def metodka(f):
    pass
