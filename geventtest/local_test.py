import gevent
from gevent.local import local

data = local()

def func1():
    data.x = 1
    print 'func1 set x 1'
    gevent.sleep(1)
    print data.x

def func2():
    data.x = 2
    print 'func2 set x 2'
    gevent.sleep(1)
    print data.x

gevent.joinall([
    gevent.spawn(func1),
    gevent.spawn(func2)])