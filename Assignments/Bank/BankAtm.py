
import Card
import BankBranch
import BankAccount
import Transaction
import time

class BankAtm:
    atmDict={}
    def __init__(self,atmCode):
        self.atmCode=atmCode

    def addCard(self,acct):
        BankAtm.atmDict[acct.card.cardNo]=acct
        
    def getAccountObj(self,cardNo):
        return self.atmDict[cardNo]

    def deposit(self,cardNo,amount):
        a1=self.getAccountObj(cardNo)
        if(not a1.isSeized):
            a1.deposit(amount)
            trans=Transaction.Transaction(time.time(),"ATM","Deposit",amount,a1.amount)
            a1.transList.append(trans)
        else:
            print("Account is seized")
        
    def withdraw(self,cardNo,amount):
        a1=self.getAccountObj(cardNo)
        if(not a1.isSeized):
            a1.withdraw(amount)
            trans=Transaction.Transaction(time.time(),"ATM","Withdraw",amount,a1.amount)
            a1.transList.append(trans)
        else:
            print("Account is seized")

    def checkBalance(self,cardNo):
        a1=self.getAccountObj(cardNo)
        if(not a1.isSeized):
            balance=a1.checkBalance()
        else:
            print("Account is seized")
        return balance

    def miniStmt(self,cardNo):
        a1=self.getAccountObj(cardNo)
        if(not a1.isSeized):
            transList=a1.transList
        else:
            print("Account is seized")
        return transList
    
    def Menu(self):
        print("Welcome to ATM")
        print("1: Deposit")
        print("2: Withdraw")
        print("3: Check Balance")
        print("4: Mini Statement")
        print ("5: Exit")
        choice=input("Enter your choice")
        return choice

'''def Menu():
    print("Welcome to ATM")
    print("1: Deposit")
    print("2: Withdraw")
    print("3: Check Balance")
    print("4: Mini Statement")
    print ("5: Exit")
    choice=input("Enter your choice")
    return choice

def main():
    atm=BankAtm("ATM-0001")
    br=BankBranch.BankBranch("B002","Bund Garden",1500,atm)
    br.createAccount("y",1550)
    br.createAccount("n",2000)
    br.createAccount("y",3000)
    choice=Menu()
    while(choice<=5):
        if(choice==1):
            cardNo=input("Enter card number: ")
            if(not BankAtm.atmDict.__contains__(cardNo) or BankAtm.atmDict[cardNo].isSeized):
                print ("Card {} does not exist or account is Seized".format(cardNo)) 
            else:
                amount=input("Enter amount to be deposited: ")
                br.atmObj.deposit(cardNo,amount)
                print br.atmObj.getAccountObj(cardNo).amount
        elif choice==2:
            cardNo=input("Enter card number: ")
            if(not BankAtm.atmDict.__contains__(cardNo) or BankAtm.atmDict[cardNo].isSeized):
                print ("Card {} does not exist".format(cardNo)) 
            else:
                amount=input("Enter amount to be withdrwan: ")
                br.atmObj.withdraw(cardNo,amount)
                print br.atmObj.getAccountObj(cardNo).amount
        elif choice==3:
            cardNo=input("Enter card number: ")
            if(not BankAtm.atmDict.__contains__(cardNo) or BankAtm.atmDict[cardNo].isSeized):
                print ("Card {} does not exist".format(cardNo)) 
            else:
                print(br.atmObj.checkBalance(cardNo))
        elif choice==4:
            cardNo=input("Enter card number: ")
            if(not BankAtm.atmDict.__contains__(cardNo) or BankAtm.atmDict[cardNo].isSeized):
                print ("Card {} does not exist".format(cardNo)) 
            else:
                print(br.atmObj.checkBalance(cardNo))
        else:
            return
        choice=Menu()
    
if __name__=='__main__':
    main()
'''
