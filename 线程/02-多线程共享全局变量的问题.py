from threading import Thread
import time

g_num = 0
# 使用一个全局变量来标记是否有进程在占用g_num
g_use = False


def work1():
    global g_num
    global g_use

    while True:
        if not g_use:
            g_use = True
            for num in range(1000000):
                g_num += 1
            g_use = False
            break


def work2():
    global g_num
    global g_use

    while True:
        if not g_use:
            g_use = True
            for num in range(1000000):
                g_num += 1
            g_use = False
            break


def main():
    print("线程开始前g_Num为:%d" % g_num)
    t1 = Thread(target=work1)
    t2 = Thread(target=work2)
    t1.start()
    t2.start()
    time.sleep(2)
    print("等待2秒以后，g_num为:%d" % g_num)


if __name__ == "__main__":
    main()
