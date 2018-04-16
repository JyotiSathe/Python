#WAP to define insufficient balance exception and raise the same when user enters
#amount to withdraw greater than avaiable balance

class WithdrawBalanceError(Exception):
    def __init__(self,amount):
        self.amount=amount
    def __str__(self):
        return "Entered amount is "+str(self.amount)

class LessThanZeroBalanceInput(WithdrawBalanceError):
    def __init__(self,amount):
        WithdrawBalanceError.__init__(self,amount)

class InsufficientBalance(WithdrawBalanceError):
    def __init__(self,amount):
        WithdrawBalanceError.__init__(self,amount)

class InsufficientBalance2(Exception):
    pass

def main():
    amount=1500
    withdrawAmount=input("Enter amount")
    try:
        if(withdrawAmount<=0):
            raise LessThanZeroBalanceInput(withdrawAmount)
        else:
            if(withdrawAmount>amount):
                raise InsufficientBalance(withdrawAmount)
            else:
                amount-=withdrawAmount
                print amount
    except LessThanZeroBalanceInput as e:
        print "Amount cannot be less than zero\n",e
    except InsufficientBalance as e:
        print "Balance is not sufficient\n",e

if __name__=='__main__':
    main()
