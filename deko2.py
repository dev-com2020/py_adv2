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