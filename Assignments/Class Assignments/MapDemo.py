def Square(x):
    return x*x

x=map(Square,range(1,30,2))
print type(x)
print x

x=map(lambda y:y*y,range(1,30,2))
print type(x)
print x
