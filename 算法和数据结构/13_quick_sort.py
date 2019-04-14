def quick_sort(lis, first, last):
    if last <= first:
        return
    # 先取出基准值
    tmp = lis[first]
    # 定义左边游标
    low = first
    # 定义右边游标
    high = last

    # 如果2个游标不重合，证明基准值的位置还未到达
    while low < high:
        # 先从右边排序，把右边小于基准值的元素移动到左边,另外在low和high之间选择一个把相等元素的跳过，否则可能出现死循环
        while low < high and lis[high] >= tmp:
            high -= 1
        # 当循环退出以后，证明上面2个条件某一个符合了。都可以把high的值放到low位置上
        lis[low] = lis[high]

        while low < high and lis[low] < tmp:
            low += 1
        lis[high] = lis[low]
    # 当这个循环退出后，证明基准值得位置能确认好
    lis[low] = tmp
    # 当这个基准值确认好以后，列表分成了2部分
    # 还需要分别对这2部分进行排序
    quick_sort(lis,first, low-1)
    quick_sort(lis, low+1, last)

lis = [11, 14, 4, 7, 24, 7, 13, 3, 50,100, 1, 11, 12, 6, 5, 9]
quick_sort(lis,0, len(lis)-1)
print(lis)