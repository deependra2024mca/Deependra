class team:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def display(self):
        print("Your name:",self.__name)
t=team("Deependra",21)
t.display()
print(t.__age)