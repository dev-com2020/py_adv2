import pickle

class foobar:
    def __init__(self):
        self.a = 35
        self.b = "tomek"
        self.c = lambda x: x * x

    def __getstate__(self):
        attributes = self.__dict__.copy()
        del attributes['c']
        return attributes

    def __setstate__(self, state):
        self.__dict__ = state
        self.c = lambda x: x * x


my_foobar_inst = foobar()

my_pickle_string = pickle.dumps(my_foobar_inst)
my_new_inst = pickle.loads(my_pickle_string)

print(my_new_inst.__dict__)