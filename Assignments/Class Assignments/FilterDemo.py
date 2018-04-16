def notDivisibleBy6(x):
    return x%2!=0 and x%3!=0

print (filter(notDivisibleBy6,range(2,25)))
print (filter(notDivisibleBy6,(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19)))
print (map(notDivisibleBy6,range(2,25)))
print (filter(lambda y:y%2!=0 and y%3!=0,range(2,25)))
