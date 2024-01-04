class Cat():
    def __init__(self, breed, age):
        self.breed = breed
        self.age = age

    @staticmethod
    def miau():
        return "Miau!"

    @classmethod
    def type(cls):
        if cls.__name__ == 'Cat':
            return "To jest jakiś kot"
        else:
            return cls.__name__

    def cat_age(self):
        return self.age

    def breed(self):
        return self.breed

    def __repr__(self):
        return "{breed}, {age}".format(breed=self.breed, age=self.age)


class Japanise_cat(Cat):
    pass


kot1 = Cat("domowy", 4)
print(kot1)
print(kot1.breed)
print(kot1.age)
# print(Cat.miau())
# print(Cat.miau)
print(kot1.miau())
print(kot1.type())
kot2 = Japanise_cat("japoński", 5)
print(kot2.type())
