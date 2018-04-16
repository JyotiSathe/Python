import threading
import time

def SimpleThread(name):
    time.sleep(3)
    print "SimpleThread"
    print name
    print threading.currentThread().getName()

def main():
    t=threading.Thread(target=SimpleThread,args=("Jyoti",))
    #,name="Interesting")
    t.start()
    t.join()
    for i in range(5):
        time.sleep(1)
        print i

if __name__=='__main__':
    main()
