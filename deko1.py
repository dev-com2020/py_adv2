def func_f(val):
    print(val)


name = func_f
func_f("SPam!")
name("To też spam!")


def div(x, y):
    return x // y


def math1(func, x, y):
    result = func(x, y)
    return result


print(math1(div, 4, 2))


def person(name):
    def greeting():
        return "O co chodzi?, "
    greet = greeting() + name + "!"
    return greet

print(person("Tomek"))


def fun_decorator(some_func):
    def wrapper():
        print("Oto dekorator wykonujący swoje zadanie.")
        for i in range(10):
            print(i)
        print("Dekorator zakończył swoje działanie, powrót do początkowo wykonywanej funkcji")
        print(some_func())
    return wrapper

def a_funct():
    text = "To jest oryginalny tekst"
    return text

a_funct = fun_decorator(a_funct)
a_funct()