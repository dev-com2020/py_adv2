# class MyClass:
#     def method(self):
#         return 1


def method(self):
    return 1


MyClass = type('MyClass', (), {'method': method})


class ClassWithAMeta(metaclass=type):
    pass


class Metaclass(type):
    def __new__(mcs, name, bases, namespace):
        return super().__new__(mcs, name, bases, namespace)

    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        return super().__prepare__(name, bases, **kwargs)

    def __init__(cls, name, bases, namespace, **kwargs):
        super().__init__(name, bases, namespace)

    def __call__(cls, *args, **kwargs):
        return super().__call__(*args, **kwargs)


class Meta(type):
    def __new__(mcs, name, bases, namespace):
        print(mcs, "Wywołano metode new METAKLASY")
        return super().__new__(mcs, name, bases, namespace)

    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        print(mcs, "Wywołano metode prepare METAKLASY")
        return super().__prepare__(name, bases, **kwargs)

    def __init__(cls, name, bases, namespace, **kwargs):
        print(cls, "Wywołano metode init METAKLASY")
        super().__init__(name, bases, namespace)

    def __call__(cls, *args, **kwargs):
        print(cls, "Wywołano metode call METAKLASY")
        return super().__call__(*args, **kwargs)


if __name__ == '__main__':
    class RevClass(metaclass=Meta):
        def __new__(cls):
            print(cls, "wywołano metodę new z RevClas")
            return super().__new__(cls)

        def __init__(self):
            print(self, "Wywołano metodę init z RevClas")
            super().__init__()

    ins = RevClass()
