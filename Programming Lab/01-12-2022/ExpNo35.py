#Create a bank account with members acc no,name,type of acc ,balaance.
# Write constructor and methods to deposit bank and withdraw from the bank.

class Bank:
    def __init__(self,accno,name,accty):
        self.accno=accno
        self.name=name
        self.accty=accty
        self.bal=0
    def showaccount(self):
        print("Account holder name",self.name)
        print("The Account no is", self.accno)
        print("Account type",self.accty)
        print("Account Balence",self.bal)

    def deposit(self,d1):
        self.bal=self.bal+d1
        return  self.bal
    def withdraw(self,w1):
        self.bal=self.bal-w1
        return self.bal

b=int(input("Enter Your Account no:"))
a=input("Enter Account name:")
c=input("Enter Account type:")
d=Bank(b,a,c)
d.showaccount()
while(True):
    print("MENU")
    print("\n 1.Deposit")
    print("\n 2.Withdraw")
    c=int(input("Enter choice:"))
    f=0
    if(c==1):
        f=int(input("Enter the amount to deposit:"))
        print("Your total bank deposit is\n ",d.deposit(f))

    elif(c==2):
        g=int(input("Enter the amount to withdraw:"))
        if(g<f):
            print("Insufficient balance")
        else:
            print("Total balance amount is:\n",d.withdraw(g))
    else:
        print("Enter valid choice")


