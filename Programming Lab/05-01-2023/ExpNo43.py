import csv
c_col=['ID','Name','Age']
dict_data=[{'ID':1,'Name':'Raoof','Age':15},
           {'ID':2,'Name':'Abina','Age':17},
           {'ID':3,'Name':'Aleena','Age':18},
           {'ID':4,'Name':'Anjaly','Age':19},
           {'ID':5,'Name':'Alan','Age':20},
           {'ID':6,'Name':'Amin','Age':41},
           {'ID':7,'Name':'Fathima','Age':22},
           {'ID':8,'Name':'Alex','Age':30},
           {'ID':9,'Name':'Arya','Age':40},
           {'ID':10,'Name':'Alfiya','Age':14}]
try:
    with open("name.csv","w")as f:
        write=csv.DictWriter(f,fieldnames=c_col)
        write.writeheader()
        for i in dict_data:
            write.writerow(i)
except IOError:
    print("Input/Output Error")
d=csv.DictReader(open("name.csv"))
print('CSV File output is : ')
for i in d:
    print(i)