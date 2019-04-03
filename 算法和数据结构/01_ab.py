 # a + b +c == 1000 && a^2 + b^2 = c^

for a in range(0,1001):

    for b in range(0,1001):
        c = 1000 - a - b
        if a+b+c == 1000 and a**2 + b**2 == c**2:
            print("a,b,c:", a, b, c)
