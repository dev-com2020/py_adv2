class A:
    def ping(self):
        print('ping', self)


class B(A):
    def pong(self):
        print('pong', self)


class C(A):
    def pong(self):
        print('PONG', self)


class D(B, C):
    def ping(self):
        super().ping()
        print('post-ping', self)

    def pingpong(self):
        self.ping()
        super().ping()
        self.pong()
        super().pong()
        C.pong(self)


print(D.mro())
d = D()
d.pong()
d.ping()
C.pong(d)


def print_mro(cls):
    print(', '.join(c.__name__ for c in cls.__mro__))

print_mro(C)
print_mro(bool)
print_mro(A)
