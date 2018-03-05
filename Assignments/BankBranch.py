import BankAccount

class BankBranch:
    
    def __init__(self,branchCode,branchName,totalAcctInBranch):
        self.branchCode=branchCode
        self.branchName=branchName
        self.totalAcctInBranch=totalAcctInBranch
        self.acctDict={}
        
    def createAccount(self,initialAmount=500):
        b=BankAccount.BankAccount(initialAmount)
        self.acctDict[b.accountNo]=b
        print self.acctDict
        print self.getAccountObj(b.accountNo).amount
    
    def getAccountObj(self,acctNo):
        #print self.acctDict[acctNo].amount
        return self.acctDict[acctNo]

    def deposit(self,acctNo,amount):
        a1=self.getAccountObj(acctNo)
        a1.deposit(amount)
        
    def withdraw(self,acctNo,amount):
        a1=self.getAccountObj(acctNo)
        a1.withdraw(amount)

    def checkBalance(self,acctNo):
        a1=self.getAccountObj(acctNo)
        return a1.checkBalance()
    
    def transfer(self,donor,acceptor,amount):
        donorObj=self.getAccountObj(donor)
        acceptorObj=self.getAccountObj(acceptor)
        donorObj.withdraw(amount)
        acceptorObj.deposit(amount)

def Menu():
    print("1:Create Account")
    print("2.Deposit Ammount")
    print("3.Withdraw Ammount")
    print("4:Check Balance")
    print("5:Transfer Money")
    print("6:Exit")
    print ("-------------------------------------------")
    choice=input("Enter which operation you want to perform: ")
    print ("-------------------------------------------")
    return choice

def main():
    br1=BankBranch("B001","KP",1000)
    #br1.createAccount(1000)
    #br1.createAccount()
    
    #br1.getAccountObj(2)
    #br1.deposit(1,200)
    #print br1.getAccountObj(1).amount
    choice=Menu()    
    while choice<=6:
        if choice==1:
            amount=input("Enter initial Amount for account to be created, minimum is 500: ")
            if(amount<500):
                print("Initial amount cannot be less than 500")
            else:
                br1.createAccount(amount)
                print br1.getAccountObj(1)
        elif choice==2:
            accountNo=input("Enter account number: ")
            if(not br1.acctDict.__contains__(accountNo)):
                print ("Account {} does not exist".format(accountNo)) 
            else:
                amount=input("Enter amount to be deposited: ")
                br1.deposit(accountNo,amount)
                print br1.getAccountObj(accountNo).amount
        elif choice==3:
            accountNo=input("Enter account number: ")
            if(not br1.acctDict.__contains__(accountNo)):
                print ("Account {} does not exist".format(accountNo)) 
            else:
                amount=input("Enter amount to be withdrawn: ")
                br1.withdraw(accountNo,amount)
                print br1.getAccountObj(accountNo).amount
        elif choice==4:
            accountNo=input("Enter account number: ")
            if(not br1.acctDict.__contains__(accountNo)):
                print ("Account {} does not exist".format(accountNo)) 
            else:
                print(br1.checkBalance(accountNo))
        elif choice==5:
            donor=input("Enter account number from which to transfer: ")
            acceptor=input("Enter account number to which to transfer: ")
            if(not br1.acctDict.__contains__(donor)):
                print ("Account {} does not exist".format(donor))  
            elif(not br1.acctDict.__contains__(acceptor)):
                print ("Account {} does not exist".format(acceptor))
            else:
                amount=input("Enter amount to be transfered: ")
                br1.transfer(donor,acceptor,amount)
                print br1.getAccountObj(donor).amount
                print br1.getAccountObj(acceptor).amount
        else:
            return
        choice=Menu()

if __name__=='__main__':
    main()
