x=int(input("Enter the First Number"))
y=int(input("Enter the Second Number"))
z=int(input("Enter the Third Number"))
if(x>=y)and(x>=z):
    largest=x
elif (y>=x)and(y>=z):
    largest=y
else:
    largest=z

print("Largest number ",largest)