#
import BankBranch
import BankAtm
def goTo(choice,br):
    if choice==1:
        BankBranch.main(br)
    elif choice==2:
        choice=br.atmObj.Menu()
        while(choice<=5):
            if(choice==1):
                cardNo=input("Enter card number: ")
                if(not BankAtm.BankAtm.atmDict.__contains__(cardNo)):
                    print ("Card {} does not exist".format(cardNo)) 
                else:
                    amount=input("Enter amount to be deposited: ")
                    br.atmObj.deposit(cardNo,amount)
                    print br.atmObj.getAccountObj(cardNo).amount
            elif choice==2:
                cardNo=input("Enter card number: ")
                if(not BankAtm.BankAtm.atmDict.__contains__(cardNo)):
                    print ("Card {} does not exist".format(cardNo)) 
                else:
                    amount=input("Enter amount to be withdrwan: ")
                    br.atmObj.withdraw(cardNo,amount)
                    print br.atmObj.getAccountObj(cardNo).amount
            elif choice==3:
                cardNo=input("Enter card number: ")
                if(not BankAtm.BankAtm.atmDict.__contains__(cardNo)):
                    print ("Card {} does not exist".format(cardNo)) 
                else:
                    print(br.atmObj.checkBalance(cardNo))
            elif choice==4:
                cardNo=input("Enter card number: ")
                if(not BankAtm.BankAtm.atmDict.__contains__(cardNo)):
                    print ("Card {} does not exist".format(cardNo)) 
                else:
                    transList=br.atmObj.miniStmt(cardNo)
                    print("Timestamp    Place    Action    Amount    Balance")
                    for trans in transList:
                        print ("{}\t{}\t{}\t{}\t{}".format(trans.timestamp,trans.where,trans.trans_type,trans.amount,trans.balance))
            else:
                return
            choice=br.atmObj.Menu()
    else:
        return

def Menu():
    print ("1: Branch")
    print ("2: ATM")
    print ("3: Exit")
    choice=input("Enter where you want to go")
    return choice

def main():
    atm1=BankAtm.BankAtm("ATM-0001")
    br1=BankBranch.BankBranch("B001","KP",1000,atm1)
    BankBranch.main(br1)
    choice=Menu()
    while(choice<3):
        goTo(choice,br1)
        choice=Menu()
        
if __name__=='__main__':
    main()
