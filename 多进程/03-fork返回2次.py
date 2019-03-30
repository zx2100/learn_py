import random
import os

a = 100
b = []

for c in range(10):
    b.append(random.randint(1, 200))

    #print(b)


sub = os.fork()

print(b)