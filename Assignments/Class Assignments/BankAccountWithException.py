#Wa simple bank account class which generates account number automatically
#and then implement method withdraw, deposit, check balance
#WA menu driven program to simulate a bank accout operations
class InsufficientBalance(Exception):
    pass

class BankAccount():
    accountNo=1
    name="SBI"
    def __init__(self,initialAmount=500):
        self.amount=initialAmount
        self.accountNo=BankAccount.accountNo
        BankAccount.accountNo+=1
        print ("Constructor")

    def deposit(self,amount):
        if(amount<=0):
            print("Enter valid amount")
        else:
            self.amount+=amount

    def withdraw(self,amount):
        if(amount<=0):
            print("Enter valid amount")
        else:
            if(amount>self.amount):
                raise InsufficientBalance
            else:
                self.amount-=amount

    def checkBalance(self):
        return self.amount


def Menu():
    print ("1:Withdraw Money")
    print ("2:Deposit Money")
    print ("3:Check Balance")
    print ("4:Exit")
    choice=input("Enter which operation you want to perform")
    return choice
        
def main():
    b1=BankAccount()
    #b2=BankAccount(1000)
    choice=Menu()
    while(choice<=4):
        if(choice==1):
            amount=input("Enter amount to be withdrawn")
            try:
                b1.withdraw(amount)
            except InsufficientBalance as e:
                print ("InsufficientBalance")
            c1=input("do you want to check balance remaining?(y/n)")
            if(c1=='y'):
                print (b1.checkBalance())
            elif(c1=='n'):
                print("Exiting")
            else:
                print("Entered option is incorrect")
        elif(choice==2):
            amount=input("Enter amount to be deposited")
            b1.deposit(amount)
        elif(choice==3):
            print (b1.checkBalance())
        elif(choice==4):
            return
        else:
            print ("Aborted...")
            return
        choice=Menu()

if __name__=='__main__':
    main()
