import datetime
import time

from multiprocessing import Process, Queue

def t(s):
    while (True):
        time.sleep(s)
        print(datetime.datetime.now().time())

def main():
    bucle = 0
    p = Process(target=t, args=(1,))
    p.start()
    
    while(bucle<10):
        time.sleep(1)
        print(p.pid)
        bucle=bucle+1

    p.terminate()
    print("fi")

__name__ == '__main__'

main()
