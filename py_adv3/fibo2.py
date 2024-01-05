import functools
import sys
import pstats
import profile


@functools.lru_cache(maxsize=128)
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
    profiler = profile.Profile(bias=2.0939406059394783e-06)
    profiler = profile.Profile()
    n = 90
    if sys.argv[-1] == 'cache':
        profiler.runcall(fibo_cached, n)
    else:
        profiler.runcall(fibo, n)

    stats = pstats.Stats(profiler).sort_stats('calls')
    stats.print_stats()
