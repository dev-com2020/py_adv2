import sys
import functools


@functools.lru_cache()
def fibo_cached(n):
    if n < 2:
        return n
    else:
        return fibo_cached(n - 1) + fibo_cached(n - 2)


def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)


if __name__ == '__main__':
    n = 30
    if sys.argv[-1] == 'cache':
        fibo_cached(n)
    else:
        fibo(n)
