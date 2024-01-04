import collections


class DoppleDict2(collections.UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)

dd = DoppleDict2(pierwszy=1)
dd['drugi'] = 2  # setitem
dd.update(trzeci=3)
print(dd)


class AnswerDict2(collections.UserDict):
    def __getitem__(self, item):
        return 100

ad = AnswerDict2(a="tomek")
print(ad)
print(ad['a'])
slownik = {}
slownik.update(ad)
print(slownik['a'])
print(slownik)

