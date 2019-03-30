def chengjie(num):
    result = 1
    i = 0
    while i < num:
        result = result*(num-i)
        i+=1
    return (result)

def chengjie2(num):
    if num < 1:
        return (1)
    return (num* chengjie2(num-1))


print


