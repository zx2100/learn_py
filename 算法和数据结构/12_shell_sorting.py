import random



def shell_sorting(lis):
    """这是一个希尔排序算法啊"""
    n = len(lis)
    gap = n // 2

    while gap > 0:
        for j in (range(gap, n)):
            i = j
            while i >= gap:
                if lis[i] < lis[i-gap]:
                    lis[i], lis[i-gap] = lis[i-gap], lis[i]
                    i -= gap
                else:
                    break
        gap //= 2
    return lis


if __name__ == "__main__":
    lis
    print(lis)
    print(shell_sorting(lis))
