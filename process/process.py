from multiprocessing import Process
import time
sum = 0

def func(name):
    time.sleep(1)
    print "hello", name, time.ctime(), p.pid

if __name__ == '__main__':
    plist = []
    for i in range(5):
        p = Process(target=func, args=(i,))
        plist.append(p)
        p.start()
    
    for p in plist:
        p.join()
    print "main end"