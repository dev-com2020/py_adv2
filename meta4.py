class InstanceCountingClass:
    created = 0
    number: int

    def __new__(cls, *args, **kwargs):
        inst = super().__new__(cls)
        inst.number = cls.created
        cls.created += 1
        return inst

    def __repr__(self):
        return f"<{self.__class__.__name__}: " f"{self.number} z {self.created}"


if __name__ == '__main__':
    instances = [InstanceCountingClass() for _ in range(5)]
    for i in instances:
        print(i)
    print(f"W sumie: {InstanceCountingClass.created}")


class NonZero(int):
    def __new__(cls, value):
        return super().__new__(cls, value) if value != 0 else None

    def __init__(self, skipped_value):
        print("Wywołano __init__")
        super().__init__()


print(type(NonZero(-12)))
print(type(NonZero(0)))
print(type(NonZero(-3.123)))

