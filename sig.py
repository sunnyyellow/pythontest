#encoding=utf-8
import signal
global sig_flag
sig_flag = 0

def handle(signum, frame):
    print("recv ", signum)
    global sig_flag
    if signum == signal.SIGUSR1:
        sig_flag = 1
    elif signum == signal.SIGUSR2:
        sig_flag = 2


def main():
    while True:
        if sig_flag == 0:
            pass
        elif sig_flag == 1:
            print "global sig_flag is " , 1
        elif  sig_flag == 2:
            print "global sig_flag is " , 2
            break

if __name__ == "__main__":
    main()



