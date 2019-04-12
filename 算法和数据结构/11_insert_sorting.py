def insert_sorting(lis):
    """这是一个插入排序算法"""
    n = len(lis)
    for j in range(n-1):
        i = j+1
        while i > 0:
            if lis[i] < lis[i-1]:
                list[i], lis[i-1] = lis[i-1], lis[i]
                i -= 1
            else:
                break
    return lis

list = [11, 14, 4, 7, 24, 7, 13, 11, 50]

print(insert_sorting(list))