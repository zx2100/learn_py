

def select_sort(list):
    """这是一个选择排序"""
    n = len(list)
    out = n - 1

    for j in range(out):
        min_index = j
        for i in range(n-j):
            if list[min_index] > list[i+j]:
                min_index = i+j

        if j != min_index:
            list[min_index], list[j] = list[j], list[min_index]

    return list

li = [1,3,4,2,7,6,5]
print(select_sort(li))