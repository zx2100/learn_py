import timeit



def test1():
    li = []
    for i in range(3000):
        li.insert(0, i)


t1 = timeit.Timer("test1()", "from __main__ import test1")
print(t1.timeit(number=1000))
