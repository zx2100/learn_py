from threading import Thread, Lock
import time


class My1(Thread):

    def run(self):
        if l1.acquire():
            print("my1 l1 is up")

        time.sleep(0.5)
        if l2.acquire():
            print ("my1 locking l2")

        l1.release()


class My2(Thread):

    def run(self):
        if l2.acquire():
            print("my2 l2 is up")

        time.sleep(0.5)
        if l1.acquire():
            print("my2 locking l1")

        l2.release()


l1 = Lock()
l2 = Lock()

m1 = My1()
m2 = My2()

m1.start()
m2.start()