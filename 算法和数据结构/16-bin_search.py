
def bin_search(lis, item):
    """2分查找"""

    n = len(lis)
    mid = n // 2
    # 如果长度小于0，表示列表为空，就返回假
    if n <= 0:
        return False
    # 如果能查找到，返回真
    if lis[mid] == item:
        return True
    # 如果找不到,判断item大于还是小于当前中间值，
    elif item < lis[mid]:
        # 小于就往左部分查找
        return bin_search(lis[0:mid], item)
    else:
        return bin_search(lis[mid+1:], item)



lis = []
for i in range (100000):
    lis.append(i)
#print(lis)


print(bin_search(lis, 19134))