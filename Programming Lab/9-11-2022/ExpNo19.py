a=int(input("Enter the no of elements:"))
list=[]

for i in range(a) :
    n = int(input("Enter the elements:"))
    list.append(n)
print("List Items",list)

for i in list:
    if(i%2==0):
        list.remove(i)
print("List after removing even items",list)




