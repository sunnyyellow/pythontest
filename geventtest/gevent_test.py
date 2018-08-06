from gevent import monkey; monkey.patch_socket()
import gevent
import socket
import time

urls = ['www.baidu.com', 'www.gevent.org', 'www.python.org']
stime = time.time()
jobs = [gevent.spawn(socket.gethostbyname, url) for url in urls]
gevent.joinall(jobs, timeout=5)
etime = time.time()
print 'cost time:', etime - stime
print [job.value for job in jobs]

def win():
    return 'You win!'

def fail():
    raise Exception('You fail!')

winner = gevent.spawn(win)
loser = gevent.spawn(fail)

print winner.started
print loser.started

try:
    gevent.joinall([winner, loser])
except Exception,e:
    print 'This will not happen: %s' %e

print winner.ready()
print loser.ready()

print winner.value
print loser.value

print winner.successful()
print loser.successful()

print loser.exception