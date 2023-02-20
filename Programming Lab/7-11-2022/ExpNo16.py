a=int(input("Enter the no of elements:"))
print("Enter the elements")
list=[]
for i in range(0,a):
    ele=int(input())
    if ele>100:
        list.append('over')
    else:
        list.append(ele)
print(list)