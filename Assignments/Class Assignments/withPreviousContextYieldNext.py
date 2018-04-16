def square(n):
    for i in range(1,n+1):
        yield i*i
n=5
s=square(n)
for i in range(n):
    print next(s)


x=[1,2,5,7,8]
y=iter(x)
for i in range(len(x)):
    print next(y)
