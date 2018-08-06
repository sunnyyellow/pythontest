import threading
import time

sum = 0
lock = threading.Lock()
def func(name, lock):
    time.sleep(1)
    print "hello", name, time.ctime()
    lock.acquire()
    sum += 10
    lock.release()



if __name__ == '__main__':
    tlist = []
    for i in range(5):
        th = threading.Thread(target=func, args=(i,))
        tlist.append(th)
        th.start()

    for t in tlist:
        t.join()
    print "main end"
        