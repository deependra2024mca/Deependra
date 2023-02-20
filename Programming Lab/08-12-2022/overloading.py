'''class team:
    def add(self,a,b):
        return self.a+self.b
    def add(self,x,y,z):
        return self.x+self.y+self.z
t=team()
print(t.add(2,4))
print(t.add(2,4,6))

class A:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(self, other):
        return self.a+other.a, self.b+other.b
    def __str__(self):
        return self.a , self.b
o1=A(2,4)
o2=A(4,8)
print(o1+o2)'''
class A:
    def __init__(self,a):
        self.a=a

    def __gt__(self, other):
        if self.a>other.a:
            return True
        else:
            return False
o1=A(18)
o2=A(81)
if(o1>o2):
    print("1st Object is greater than 2nd object")
else:
    print("2nd Object is greater than 1st object")

class A:
    def __init__(self,a):
        self.a=a

    def __lt__(self, other):
        if self.a<other.a:
            return True
        else:
            return False
o1=A(18)
o2=A(81)
if(o1<o2):
    print("1st Object is lesser than 2nd object")
else:
    print("2nd Object is lesser than 1st object")
