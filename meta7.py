from typing import Any
import inflection


class CaseInterDict(dict):
    def __setitem__(self, key: str, value: Any):
        super().__setitem__(key, value)
        super().__setitem__(inflection.underscore(key), value)


class CaseInterMeta(type):
    @classmethod
    def __prepare__(metacls, name, bases):
        return CaseInterDict()


class User(metaclass=CaseInterMeta):
    def __init__(self, firstName: str, lastName: str):
        self.firstName = firstName
        self.lastName = lastName

    def getDisplayName(self):
        return f"{self.firstName} {self.lastName}"

    def greetUser(self):
        return f"Witaj, {self.getDisplayName()} !"


print(User.__dict__)

user = User("Jan", "Kowalski")
print(user.getDisplayName())
print(user.get_display_name())
print(user.greetUser())
print(user.greet_user())


