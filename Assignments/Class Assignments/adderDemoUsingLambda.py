def Increment(n):
    return lambda x:x+n

increment_by_5=Increment(5)
increment_by_10=Increment(10)
increment_by_100=Increment(100)

print increment_by_5(1)
print increment_by_10(30)
print increment_by_100(500)
