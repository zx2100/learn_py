from multiprocessing import Process, Queue
import time
import random


def write(q):
    for value in ["A", "B", "C", "D", "E"]:

        if not q.full():
            print("OK，开始写入数据%s。" % value)
            q.put(value)
            time.sleep(random.randint(0, 2))


def read(queue):
    while True:
        if not queue.empty():
            print("读到数据:%s,当前队列长度为：%s" % (str(queue.get()), str(queue.qsize())))
        else:
            time.sleep(1)


def main():
    q = Queue()
    p1 = Process(target=write, args=(q,))
    p2 = Process(target=read, args=(q,))

    p1.start()
    p2.start()
    p2.join()


if __name__ == "__main__":
    main()
