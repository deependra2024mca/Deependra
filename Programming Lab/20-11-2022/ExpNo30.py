def longestLength(a):
    max1 = len(a[0])
    temp = a[0]


    for i in a:
        if (len(i) > max1):
            max1 = len(i)
            temp = i

    print("The Longest word is:", temp,
          " and length is ", max1)


a=[]
n = int(input("Enter the no words:"))
print("Enter the Words:")
for j in range(0,n):
    ele=input()
    a.append(ele)
longestLength(a)