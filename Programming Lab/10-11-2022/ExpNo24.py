str=input("Enter the String")
dict={}
str = str.split()

for i in str:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

print(dict)
for m,n in dict.items():
    print(m,n)