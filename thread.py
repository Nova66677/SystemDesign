import threading
import time


def countUp(n):

    for i in range(0, n+1):
        print("Running thread 1...")
        print(i)
        time.sleep(1)


def countDown(n):

    for i in range(n, -1, -1):
        print("Running thread 2...")
        print(i)
        time.sleep(1)

t1 = threading.Thread(target=countUp, args=(5,))
t2 = threading.Thread(target=countDown, args=(5,))
t2.start()
t1.start()