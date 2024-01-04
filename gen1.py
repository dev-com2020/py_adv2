def my_gen(x):
    while x:
        x -= 1
        yield x


mygen = my_gen(5)
print(mygen)
print(next(mygen))
print("Inne czynności...")
print(next(mygen))
print(next(mygen))
print(next(mygen))
print(next(mygen))
# print(next(mygen))

gen = (x for x in range(10))

for i in gen:
    print(i)

