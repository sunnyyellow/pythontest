#encoding=utf-8
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
import concurrent.futures
import time
def task1():
    print "task1 start..", time.ctime()
    time.sleep(5)
    print "task1 sleep 5s", time.ctime()
    return "task1 end"

def task2():
    print "task2 start..", time.ctime()
    time.sleep(8)
    print "task2 sleep 8s", time.ctime()
    return "task2 end"

def task(name, t):
    print "task[%s] starts sleep %s ..." % (name, t), time.ctime()
    time.sleep(t)
    print "task[%s] ends" % name, time.ctime()
    return "task[%s]" % name

futures = []
def main():
    with ThreadPoolExecutor(max_workers=5) as e:
        r = e.submit(task, 1, 5)
        futures.append(r)
        r = e.submit(task, 2, 8)
        futures.append(r)

        # 此方法是block的，当所有的结果都返回时，才会返回结果并打印。
        '''
        for future in futures:
            print future.result(), time.ctime()
        '''

        #只要有线程结果，就会有结果返回
        for future in as_completed(futures):
            print future.result(), time.ctime()
            break
        
        print "complete over", time.ctime()
        return
        #
        '''
        result = concurrent.futures.wait(futures, timeout= 3,  return_when=concurrent.futures.FIRST_COMPLETED)
        fs = result[0]
        for f in fs:
            print f.result(), time.ctime()
        print "wait over", time.ctime()
        return
        '''

if __name__ == "__main__":
    main()
    print "main over", time.ctime()
