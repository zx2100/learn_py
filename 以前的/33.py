
class Test(object):

    def __init__(self, value):
        self.value = value


    def __getattribute__(self, item):

        if item == "valuee":
            return ("error")
        else:
            return(object.__getattribute__(self,item))


t = Test("admin")

print(t.value)
