import threading
import time


def test():

    print("多线程")


def main():
    for num in range(5):
        t = threading.Thread(target=test)
        time.sleep(1)
        t.start()



if __name__ == "__main__":
    main()
