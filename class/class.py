import time
'''
    can call self function in __init__() 
'''
class A:
    def __init__(self, name):
        self.name = name
        self._print()
        self._sleep()
    def _print(self):
        print self.name
    def _sleep(self):
        while True:
            time.sleep(3)
            print "---", time.time()

a = A("amy")