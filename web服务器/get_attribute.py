
class Foo(object):

    def __init__(self):
        self.a = 20
        self.b = 30

    def __getattribute__(self, item):
        if item == "a":
            return 10
        object.__getattribute__(self, item)




print(Foo().b)

