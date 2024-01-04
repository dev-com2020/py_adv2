import pickle


# pickle.dumps()
# pickle.dump()
# pickle.loads()
# pickle.load()

class example:
    a_number = 35
    a_string = "Tomek"
    a_list = [1, 2, 3]
    a_dict = {'pierwszy': "a", "drugi": [2, 3, 4]}
    a_tuple = (44, 66)


obj = example()

my_pickled_obj = pickle.dumps(obj)
print(f"To jest obiekt pickle: {my_pickled_obj}")

obj.a_dict = None

my_unpickled_object = pickle.loads(my_pickled_obj)
print(f"To jest obiekt pickle - odzysk: {my_unpickled_object.a_dict}")

import dill

square = lambda x: x * x
my_pickle_lambda = dill.dumps(square)
print(my_pickle_lambda)