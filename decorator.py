def dec1(func):
    def inner():
        print "decorator 1========="
        func()
        print "decorator 1========= end"

    return inner

def dec2(func):
    def inner():
        print "decorator 2========="
        func()
        print "decorator 2========= end"
    return inner

@dec1
@dec2
def f():
	print "base func......"

f()