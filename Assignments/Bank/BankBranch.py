import BankAccount
import Card
import BankAtm
import Transaction
import time

class BankBranch:
    
    def __init__(self,branchCode,branchName,totalAcctInBranch,atmObj):
        self.branchCode=branchCode
        self.branchName=branchName
        self.totalAcctInBranch=totalAcctInBranch
        self.atmObj=atmObj
        self.acctDict={}
        
    def createAccount(self,isIssued,initialAmount=500):
        acct=BankAccount.BankAccount(initialAmount)
        self.acctDict[acct.accountNo]=acct
        if(isIssued=="y"):
            acct.card=Card.Card("MasterCard","03/16","11/35")
            self.atmObj.addCard(acct)
            print "Generated Card Number is {}".format(acct.card.cardNo)
        print self.acctDict
        print self.getAccountObj(acct.accountNo).amount
        
        
    def getAccountObj(self,acctNo):
        #print self.acctDict[acctNo].amount
        return self.acctDict[acctNo]

    def deposit(self,acctNo,amount):
        a1=self.getAccountObj(acctNo)
        if(not a1.isSeized):
            a1.deposit(amount)
            trans=Transaction.Transaction(time.time(),"Branch","Deposit",amount,a1.amount)
            a1.transList.append(trans)
        else:
            print("Account is seized")
        
    def withdraw(self,acctNo,amount):
        a1=self.getAccountObj(acctNo)
        if(not a1.isSeized):
            a1.withdraw(amount)
            trans=Transaction.Transaction(time.time(),"Branch","Withdraw",amount,a1.amount)
            a1.transList.append(trans)
        else:
            print("Account is seized")

    def checkBalance(self,acctNo):
        a1=self.getAccountObj(acctNo)
        if(not a1.isSeized):
            balance=a1.checkbalance()
        else:
            print("Account is seized")
        return balance
    
    def transfer(self,donor,acceptor,amount):
        donorObj=self.getAccountObj(donor)
        acceptorObj=self.getAccountObj(acceptor)
        if(not donorObj.isSeized and not acceptorObj.isSeized):
            donorObj.withdraw(amount)
            acceptorObj.deposit(amount)
        else:
            print("Either one or both accounts are seized")

def Menu():
    print("1:Create Account")
    print("2.Deposit Ammount")
    print("3.Withdraw Ammount")
    print("4:Check Balance")
    print("5:Transfer Money")
    print("6:Close Account")
    print("7:Seize Account")
    print("8:Exit")
    print ("-------------------------------------------")
    choice=input("Enter which operation you want to perform: ")
    print ("-------------------------------------------")
    return choice

def main(br1):
    #atm1=BankAtm.BankAtm("ATM-0001")
    #br1=BankBranch("B001","KP",1000,atm1)
    
    #br1.createAccount(1000)
    #br1.createAccount()
    
    #br1.getAccountObj(2)
    #br1.deposit(1,200)
    #print br1.getAccountObj(1).amount
    choice=Menu()    
    while choice<8:
        if choice==1:
            amount=input("Enter initial Amount for account to be created, minimum is 500: ")
            if(amount<500):
                print("Initial amount cannot be less than 500")
            else:
                isIssued=input("Do you want to get atm? (y/n)")
                br1.createAccount(isIssued,amount)
                print br1.getAccountObj(1)
        elif choice==2:
            accountNo=input("Enter account number: ")            
            if(not br1.acctDict.__contains__(accountNo) or br1.acctDict[accountNo].isSeized):
                print ("Account {} does not exist or is seized".format(accountNo)) 
            else:
                amount=input("Enter amount to be deposited: ")
                br1.deposit(accountNo,amount)
                print br1.getAccountObj(accountNo).amount
        elif choice==3:
            accountNo=input("Enter account number: ")
            if(not br1.acctDict.__contains__(accountNo) or br1.acctDict[accountNo].isSeized):
                print ("Account {} does not exist or is seized".format(accountNo)) 
            else:
                amount=input("Enter amount to be withdrawn: ")
                br1.withdraw(accountNo,amount)
                print br1.getAccountObj(accountNo).amount
        elif choice==4:
            accountNo=input("Enter account number: ")
            if(not br1.acctDict.__contains__(accountNo) or br1.acctDict[accountNo].isSeized):
                print ("Account {} does not exist or is seized".format(accountNo))
            else:
                print(br1.checkBalance(accountNo))
        elif choice==5:
            donor=input("Enter account number from which to transfer: ")
            acceptor=input("Enter account number to which to transfer: ")
            if(not br1.acctDict.__contains__(donor) or br1.acctDict[donor].isSeized):
                print ("Account {} does not exist or is seized".format(donor))
            if(not br1.acctDict.__contains__(acceptor) or br1.acctDict[acceptor].isSeized):
                print ("Account {} does not exist or is seized".format(acceptor))
            else:
                amount=input("Enter amount to be transfered: ")
                br1.transfer(donor,acceptor,amount)
                print br1.getAccountObj(donor).amount
                print br1.getAccountObj(acceptor).amount
        elif choice==6:
            accountNo=input("Enter account number: ")
            if(not br1.acctDict.__contains__(accountNo) or br1.acctDict[accountNo].isSeized):
                print ("Account {} does not exist or is seized and cannot be closed".format(accountNo))
            else:
                print("Closing Balance: {}".format(br1.getAccountObj(accountNo).amount))
                del br1.acctDict[accountNo]

        elif choice==7:
            accountNo=input("Enter account number: ")
            if(not br1.acctDict.__contains__(accountNo) or br1.acctDict[accountNo].isSeized):
                print ("Account {} does not exist or is seized already".format(accountNo))
            else:
                br1.getAccountObj(accountNo).isSeized=True
                print ("Account {} is seized now".format(accountNo)) 
        else:
            return br1
        choice=Menu()

if __name__=='__main__':
    main()
