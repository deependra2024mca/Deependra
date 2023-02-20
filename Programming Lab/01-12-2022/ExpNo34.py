#Create rectangle class with attributes length an bredth and methods to find area and perimeter.
# Compare 2 rectangle objects by there area.

class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def area(self):
        return self.breadth*self.length
    def perimeter(self):
        return 2*(self.length+self.breadth)

l=int(input("Enter the length:"))
b=int(input("Enter the breadth:"))
o=Rectangle(l,b)
x=o.area()
y=o.perimeter()
print("Area=",x)
print("Perimeter=",y)

l1=int(input("Enter the length:"))
b1=int(input("Enter the breadth:"))
p=Rectangle(l1,b1)
x1=p.area()
y1=p.perimeter()
print("Area=",x1)
print("Perimeter=",y1)

if(x>x1):
    print("First rectangle is greater than second rectangle")
else:
    print("Second rectangle is greater than first rectangle")




