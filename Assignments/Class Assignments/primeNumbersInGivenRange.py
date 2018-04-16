#wa generator which returns prime numbers in the given range

import check_prime_numbers

def getPrime(start_range,end_range):
    for i in xrange(start_range,end_range):
        yield check_prime_numbers.isPrime(i)
        

def main():
    start_range=input("Enter start range")
    end_range=input("Enter End Range")
    n=getPrime(start_range,end_range)
    for i in xrange(start_range,end_range):
        if(next(n)):
            print i
        else:
            continue

if __name__=='__main__':
    main()
