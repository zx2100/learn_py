import threading
import random

# 定义一个全局字典，线程名称做为KEY
g_dit = {}

def get_something():
    g_dit[threading.current_thread()] = random.randint (1, 40)

    task1()
    task2()
    task1()
    task2()

def task1():
    some = g_dit[threading.current_thread()]
    print ("当前线程%s,其some变量为%s"%(str(threading.current_thread()), some))

def task2():
    some = g_dit[threading.current_thread()]
    print ("当前线程%s,其some变量为%s"%(str(threading.current_thread()), some))

def main():
    t1 = threading.Thread(target=get_something)
    t2 = threading.Thread(target=get_something)
    t1.start()
    t2.start()



if __name__ == "__main__":
    main()
