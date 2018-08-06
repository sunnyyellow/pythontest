#encoding=utf-8
#自定义exception
class TestError(Exception):
    def __init__(self, arg):
        Exception.__init__(self, arg)
try:
    raise TestError("just test")
except Exception,e:
    print type(e).__name__