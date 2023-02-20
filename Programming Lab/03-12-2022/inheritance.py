'''class animal:
    def speak(self):
        print("Animal Speaks")

class dog(animal):
    def bark(self):
        print("Dog barks")

d=dog()
d.speak()
d.bark()

class Mother:
    mothername=""
    def mother(self):
        print(self.mothername)
class Father:
    fathername=""
    def father(self):
        print(self.fathername)
class daughter(Mother,Father):
    def parents(self):
        print("Mother:",self.mothername)
        print("Father:",self.fathername)

d=daughter()
d.fathername="abcde"
d.mothername="edsfg"
d.parents()

class grandfather:
    def __init__(self,gfname):
        self.gfname=gfname
class father(grandfather):
    def __init__(self,fname,gfname):
        self.fname=fname
        grandfather.__init__(self,gfname)
class daughter(father):
    def __init__(self,dname,fname,gfname):
        self.dname=dname
        father.__init__(self,fname,gfname)
    def show(self):
        print("Grandfather name:",self.gfname)
        print("Father name:",self.fname)
        print("Daughter name:",self.dname)

d=daughter("abc","def","ghi")
d.show()
class Father:
    def father(self):
        fathername=""
        print(self.fathername)

class Daughter1(Father):
    def daughter(self):
        daughter=""
        print("Daughter:",self.daughter())
class Daughter2(Father):
    def daughter2(self):
        daughter2=""
        print("Daughter2:",self.daughter2())

d=Daughter1()
f=Daughter2()
daughter="abcd"
daughter2="efgh"
d.daughter()
f.daughter2()


class school:
    def fun(self):
        print("School")

class student1(school):
    def fun2(self):
        print("Student 1")
class student2(school):
    def fun3(self):
        print("Student 2")
class mca(student1,student2):
    def fun4(self):
        print("MCA")
d=mca()
d.fun()
d.fun2()
d.fun3()
d.fun4()'''

class animal:
    def sound(self):
        print("Animal make sound")

