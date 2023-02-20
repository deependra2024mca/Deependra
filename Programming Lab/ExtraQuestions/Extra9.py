list = [0,3,5,8,10,11,44]
print("List : ", list)
length = len(list)
temp = list[0]
list[0] = list[length - 1]
list[length - 1] = temp
print("List after Swapping:",list)