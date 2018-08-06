
class Father(object):
    def __init__(self,name):
        self.name = name
    def sprint(self):
        print self.name
    def play(self):
        print self.name, 'play'

    
class Child(Father):
    def __init__(self,name):
        super(Child, self).__init__(name)
        #super(ProtoSession, self).__init__(service, cmd, glt)
    def play(self):
        print self.name, 'child play'

f = Father('amy')
f.play()
c = Child('amy')
c.play()