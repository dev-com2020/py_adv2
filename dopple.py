class DoppleDict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)


# slownik['klucz'] = 3 # __setitem__

dd = DoppleDict(pierwszy=1)
dd['drugi'] = 2  # setitem
dd.update(trzeci=3)
print(dd)


class AnswerDict(dict):
    def __getitem__(self, item):
        return 100

ad = AnswerDict(a="tomek")
print(ad)
print(ad['a'])
slownik = {}
slownik.update(ad)
print(slownik['a'])
print(slownik)