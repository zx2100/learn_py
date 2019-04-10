

def bubble_sort(list):
    """冒泡排序"""
    # 这是控制循环次数，在冒泡
    n = len(list)
    for j in range(n):
        # 用于从左边起，把最大的数，移动到最右边
        # 如果经过一次循环都没有需要移动的元素，则认为已经排好顺序，就没必要再次循环了
        count = False
        for i in range(n-1-j):
            # 判断当前元素和下一个元素对比，如果大于下一个元素，就交换位置
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                count = True
        if count is False:
            return list
    return list


test = [1, 1, 2, 3, 4, 5]

print(bubble_sort(test))
