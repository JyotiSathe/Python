

class ShapeManager:
    def __init__(self):
        pass
    
    def Draw(self,obj):
        obj.Draw()

class Shape:
    def Draw():
        print("Shape Draw")

class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    
    def Draw(self):
        print("Rectangle Draw")
        print self.length
        print self.breadth

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def Draw(self):
        print ("Circle Draw")
        print self.radius

def main():
    rect=Rectangle(10,10)
    cr=Circle(5)
    sh=ShapeManager()
    sh.Draw(rect)
    sh.Draw(cr)

if __name__=='__main__':
    main()
