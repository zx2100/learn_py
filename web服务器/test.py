class Foo(object):

    def __init__(self):
        self.a = self
        self.b = self
        self.c = self


    def __getattr__(self, item):
        print("没有此数值")
        return self


    def __getattribute__(self, item):
        print("Y")
        object.__getattribute__(item)

    def __str__(self):
        return "有点问题"





print(Foo().a.b.c)