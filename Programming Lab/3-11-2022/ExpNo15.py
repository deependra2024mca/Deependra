list1=[]
n = int(input("Enter number of elements : "))
for i in range(0, n):
    i = int(input())
    list1.append(i)  # adding the element
print(list1)
list2=[]
k = int(input("Enter number of elements : "))
for i in range(0, k):
    i = int(input())
    list2.append(i)  # adding the element
print(list2)
total=0
final=0
a=len(list1)
b=len(list2)
if(a==b):
    print("list1 and list2 are of same length")

for i in range(0, len(list1)):
    total = total + list1[i]
print("sum of list1 is:",total)

for j in range(0,len(list2)):
    final=final+list2[j]
print("sum of list2 is:",final)
z=total+final

print("sum of 2 lists:",z)
if(total==final):
    print("list sums to the same value")
else:
    print("sum of both list aren't the same")
c=list(set(list1).intersection(list2))
print("common elements are:",c)