from threading import Thread, Lock


g_num = 0


def work1(lock):
    global g_num
    # True表示堵塞 即如果这个锁在上锁之前已经被上锁了，那么这个线程会在这里一直等待到解锁为止
    # False表示非堵塞，即不管本次调用能够成功上锁，都不会卡在这,而是继续执行下面的代码
    lock_flag = lock.acquire()
    for num in range(1000000):
        g_num += 1
    if lock_flag:
        lock.release()
    print("线程1完成后，g_num结果为%d" % g_num)


def work2(lock):
    global g_num
    lock_flag = lock.acquire(True)

    for num in range(1000000):
        g_num += 1
    if lock_flag:
        lock.release()
    print("线程2完成后，g_num结果为%d" % g_num)


def main():
    print("线程开始前g_Num为:%d" % g_num)
    mutex = Lock()

    t1 = Thread(target=work1, args=(mutex,))
    t2 = Thread(target=work2, args=(mutex,))
    t1.start()
    t2.start()


if __name__ == "__main__":
    main()
