import time
from threading import Thread
from threading import Lock

threads=[]
data=0
lock=Lock()

def get_job():
    global data
    lock.acquire()
    data+=1
    #x=data
    time.sleep(0.1)
    lock.release()
    #return x
    return data

def process_job():
    print get_job()

for i in range(100):
    t=Thread(target=process_job)
    threads.append(t)
    t.start()

for thread in threads:
    thread.join()
