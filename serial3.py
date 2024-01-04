import pickle
import bz2

my_string = """
W krainie kodu, gdzie logika gra,
Python wije się pośród znaków spa.
Z wdziękiem skryptów, tworzy obrazy,
Zwinnie jak wąż, przez błędy prąży.

Zmiennych rzeka, funkcji ocean,
W języku tym piękno i pasja płoną.
Wciąż się rozwija, niczym baśń,
Python - to wiedzy bezcenny dar.
"""

pickled = pickle.dumps(my_string)
compressed = bz2.compress(pickled, compresslevel=9)
print(len(my_string))
print(len(compressed))
print(len(pickled))

