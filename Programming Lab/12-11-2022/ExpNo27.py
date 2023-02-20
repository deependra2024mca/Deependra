str=input("Enter a string: ")
if str[-3:] == 'ing':
    print("The new string is",str + "ly")
else:
    print("The new string is",str + "ing")
