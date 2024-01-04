class UpperAttrMetaclass(type):
    def __new__(cls, clsname, bases, dct):
        uppercase_attr = {}
        for name, val, in dct.items():
            if not name.startswith("__"):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val
        return type.__new__(cls, clsname, bases, uppercase_attr)


class Tomek(metaclass=UpperAttrMetaclass):
    imie = 'tomek'


print(hasattr(Tomek, 'imie'))
print(hasattr(Tomek, 'IMIE'))
