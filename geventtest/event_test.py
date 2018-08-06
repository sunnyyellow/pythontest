import gevent
from gevent.event import Event

evt = Event()

def setter():
    print 'Wait for me'
    gevent.sleep(3)
    print 'OK, I am done'
    evt.set()

def waiter(id):
    print '[%s] wail for you'%id
    evt.wait()
    print '[%s] finish waiting!'%id

gevent.joinall([
    gevent.spawn(setter),
    gevent.spawn(waiter, 1),
    gevent.spawn(waiter, 2),
    gevent.spawn(waiter, 3)
])