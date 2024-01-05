import timeit


def test_list():
    return list(range(10000))


def test_list_compreh():
    return [i for i in range(10000)]


def test_app():
    x = []
    for i in range(10000):
        x.append(i)
    return x


def benchmark(function, number=100, repeat=10):
    times = timeit.repeat(function, number=number, globals=globals())
    time = min(times) / number
    print('%d loops, best of %d: %9.6fs :: %s' % (number, repeat, time, function))


if __name__ == '__main__':
    benchmark('test_list()')
    benchmark('test_list_compreh()')
    benchmark('test_app()')
