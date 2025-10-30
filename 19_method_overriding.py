class Shape:
    def __init__(self,l,w):
        self.l=l
        self.w=w
        print(self.l,self.w)
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self,l,w):
        super().__init__(l,w)
        #self.l=l
        #self.w=w
        print("override",self.l,self.w)
    
    def area(self):
        return self.l * self.w
    
class Triangle(Shape):
    def __init__(self,l,w,h):
        self.h =h
        super().__init__(l,w)
        #self.l=l
        #self.w=w
        print("override-triangle",self.l,self.w)

    def area(self):
        return self.l * self.w * self.h
    
class Circle(Shape):
    def __init__(self,radius):
        self.r =radius
        print("override-circle",self.r)
    def area(self):
        return self.r**2 *3.1416
r =Rectangle(10,20)
print(r.area())

circle =Circle(10)
print(circle.area())
