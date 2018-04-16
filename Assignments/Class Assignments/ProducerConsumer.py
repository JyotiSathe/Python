from threading import Event, Thread
import time
data=[]
size=0
producer_event=Event()
consumer_event=Event()

def read():
    global data
    global producer_event
    global consumer_event
    global size
    while True:
        producer_event.wait()
        print "\nConsumed",data[0]
        del data[0]
        size=size-1
        consumer_event.set()
        producer_event.clear()

def write():
    global data
    global producer_event
    global consumer_event
    global size
    while True:
        x=input("Enter data")
        data.append(x)
        size=size+1
        producer_event.set()
        if size==5:
            consumer_event.wait()
            consumer_event.clear()

def main():
    consumer=Thread(target=read)
    producer=Thread(target=write)
    consumer.start()
    producer.start()
    consumer.join()
    producer.join()
    print "done"

if __name__=='__main__':
    main()
