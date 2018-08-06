import os
pid = os.fork()
if pid == 0:
	print "child pid = ", os.getpid()
else:
	print "parent pid = ", os.getpid(), ", child pid = ", pid 