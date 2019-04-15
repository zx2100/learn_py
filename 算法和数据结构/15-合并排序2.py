def merge_sort(lis):
    """合并排序"""
    # 判断列表是否只有一个元素
    n = len(lis)
    if n <= 1:
        return lis

    mid = n // 2
    # 左边部分
    left = merge_sort(lis[:mid])
    # 右边部分
    right = merge_sort(lis[mid:])

    # 合并左右
    l, r = 0, 0
    result = []

    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]

    return result





lis = [3, 1, 4, 2]
print(lis)
print(merge_sort(lis))