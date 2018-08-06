#encoding=utf-8
from greenlet import greenlet
#消费者、生产者模型
def consumer():
    last = ''
    while True:
        recv = pro.switch(last)
        if recv is not None:
            print "Consume %s" % recv
            last = recv

def producer(n):
    con.switch()
    x = 0
    while x < n:
        x += 1
        print "Produce %s" % x
        last = con.switch(x)
        print "last produce: %s" % last

pro = greenlet(producer)
con = greenlet(consumer)
pro.switch(5)