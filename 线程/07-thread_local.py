import threading

local_t = threading.local()



def task1():
    current_name = local_t.student
    print("%s in %s" % (current_name, threading.current_thread().name))

def get_student(name):

    local_t.student = name
    task1()

def main():
    t1 = threading.Thread(target=get_student, args=("apple", ), name="Thread-A")
    t2 = threading.Thread(target=get_student, args=("banana",), name="Thread-B")
    t1.start()
    t2.start()


if __name__ == "__main__":
    main()
