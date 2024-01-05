import tracemalloc

class Spam(object):
    index = 0
    cache = {}

    def __init__(self):
        Spam.index += 1
        self.cache[Spam.index] = self

class Eggs(object):
    eggs = []

    def __init__(self):
        self.eggs.append(self)


if __name__ == '__main__':
    n = 200000
    spam = Spam()

    tracemalloc.start()

    snapshot_a = tracemalloc.take_snapshot()
    for i in range(n):
        Spam()

    Spam.cache = {}
    snapshot_b = tracemalloc.take_snapshot()
    for i in range(n):
        a = Eggs()
        b = Eggs()
        a.b = b
        b.a = a

    Eggs.eggs = []
    snapshot_c = tracemalloc.take_snapshot()

    print('Pierwszy wyciek')
    statistics = snapshot_b.compare_to(snapshot_a, 'lineno')
    for statistic in statistics[:10]:
        print(statistic)
    print('Drugi wyciek')
    statistics = snapshot_c.compare_to(snapshot_b, 'lineno')
    for statistic in statistics[:10]:
        print(statistic)

