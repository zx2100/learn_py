class c2():
    data = 'hello'

    def __init__(self, x='30'):
        self.str = x

    def f2(self,y):
        f1 = self.data
        f3 = self.str
        print(f1,f3,y)

a1 = c2(1)
a2 = a1.f2(10)
