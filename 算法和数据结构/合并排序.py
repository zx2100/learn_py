import random

def merge_sort(lis):
    """
    算法核心思想:先分组，在重组
    1.递归分解到只有单个元素
    2.单个元素重组

    """

    n = len(lis)
    # 如果列表长度为1，可以直接返回了
    if n == 1:
        return lis
    mid = n // 2
    # 当分解到1的时候，就不在往下分解，然后开始重组

    left = merge_sort(lis[:mid])
    right = merge_sort(lis[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    l, r = 0, 0
    # 如果l或者r的长度大于列表长度，即代表列表有多个数据需要判断
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1

    # 当循环退出后，代表left或right有一个是到尾了，需要把2个列表剩下的加起来
    result += left[l:]
    result += right[r:]
    return  result




if __name__ == "__main__":
    lis = []
    for i in range(1000):
        lis.append(random.randint(1, 467))
print(lis)
print(merge_sort(lis))