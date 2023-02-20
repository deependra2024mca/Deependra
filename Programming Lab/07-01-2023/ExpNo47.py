list1=[]
list2=["Windows","Linux"]
for item in list2:
    for ele in item:
        result=ord(ele)
        list1.append(result)
print(list1)