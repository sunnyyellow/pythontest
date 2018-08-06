from greenlet import greenlet

def test1():
    print 1
    gr2.switch(1)
    print 2

def test2(x):
    print 3
    gr1.switch()
    print 4

gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.switch()