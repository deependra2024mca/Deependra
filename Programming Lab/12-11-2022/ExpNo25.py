color_list1=input("Enter the colors in list 1 :")
color_list2=input("Enter the colors in list 2 :")
list1=color_list1.split()
list2=color_list2.split()
list3=[]

print("Color List 1:",list1)
print("Color List 2:",list2)

for i in list1:
    if i not in list2:
        list3.append(i)
print("Color from Color List 1 not contain in Color List 2:",list3)
