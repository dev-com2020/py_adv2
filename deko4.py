class Cat():
    def __init__(self, breed, age):
        self.breed = breed
        self.age = age

    def cat_age(self):
        return self.age

    def breed(self):
        return self.breed

    def __repr__(self):
        return "{breed}, {age}".format(breed=self.breed, age=self.age)
