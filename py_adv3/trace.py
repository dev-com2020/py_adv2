import tracemalloc

if __name__ == '__main__':
    tracemalloc.start()

    x = list(range(1000000))

    import os
    import sys
    import asyncio

    snapshot = tracemalloc.take_snapshot()
    for statistic in snapshot.statistics('lineno')[:10]:
        print(statistic)
