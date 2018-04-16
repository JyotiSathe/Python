import pickle
class Human:
    def __init__(self):
        self.name="Jyoti"
        self.age=23
        
fd=open("F:/Python/serialized.txt","ab")

list1=[1,2,3]
dict1={"a":1,"b":2}
obj=Human()
pickle.dump(list1,fd)
pickle.dump(dict1,fd)
pickle.dump(obj,fd)
fd.close()

fd=open("F:/Python/serialized.txt","rb")
try:
    while True:
        x = pickle.load(fd)
        if isinstance(x,Human):
            print x.__dict__
            print x.name
            print x.age
        else:
            print x
            
except EOFError as e:
    fd.close()
