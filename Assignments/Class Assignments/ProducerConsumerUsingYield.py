import random

def consume():
    while True:
        data=yield
        print("Received : {}".format(data))

def produce(consumer):
    while True:
        data=random.randint(1,1000)
        print("Sent : {}".format(data))
        consumer.send(data)
        yield

def main():
    consumer=consume()
    consumer.send(None)
    producer =produce(consumer)
    for _ in range(3):
        next(producer)

if __name__=='__main__':
    main()
