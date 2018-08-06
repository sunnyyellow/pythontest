#encoding=utf-8


class A:
    def __init__(self):
        raise Exception("test error")
        self.name = "amy"
    def prints(self):
        print self.name
    
    def run(self):
        f(self)

def f(s):
    if hasattr(s, 'prints'):
        print "self has prints"
    s.prints()

a = A()
a.run()
ret = hasattr(A, 'print')
print ret