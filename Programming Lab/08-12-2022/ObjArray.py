class A:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def sum(self):
        print(self.a+self.b)
list=[]

list.append(A(2,4))
list.append(A(4,8))
list.append(A(8,14))
list.append(A(17,18))

for i in list:
    i.sum()