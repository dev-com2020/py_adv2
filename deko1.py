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