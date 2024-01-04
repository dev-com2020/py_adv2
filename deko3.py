def check_arg(func):
    def wrapper(*args):
        for num in args:
            if type(num) != int:
                raise TypeError("Argument nie jest liczbą")
            elif num <= 0:
                raise ValueError("Argument nie jest dodatni")
            else:
                return func(*args)
    return wrapper


from math import pi


@check_arg
def circle_m(radius):
    circle = 2 * pi * radius
    area = pi * radius * radius
    diameter = 2 * radius
    return (diameter, circle, area)


d, c, a = circle_m(6)
print(d, c, a)
