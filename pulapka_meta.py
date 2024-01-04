from unittest.mock import Mock

class Nonsense(metaclass=Mock):
    pass


print(Nonsense)
Nonsense()