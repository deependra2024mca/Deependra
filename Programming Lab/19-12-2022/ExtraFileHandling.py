f=open("demofile.txt","w")
f.write("I have deleted the orginal content")
f.close()

f=open("demofile.txt","r")
print(f.read())
f.close()
