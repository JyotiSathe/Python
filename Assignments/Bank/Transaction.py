

class Transaction:
    def __init__(self,timestamp,where,trans_type,amount,balance):
        self.timestamp=timestamp
        self.where=where
        self.trans_type=trans_type
        self.amount=amount
        self.balance=balance
