

class Card:
    cardNo=1000
    cvv=510
    def __init__(self,typeOfCard,issuedDate,expiryDate):
        self.cardNo=Card.cardNo
        self.cvv=Card.cvv
        Card.cardNo+=1
        Card.cvv+=1
        self.typeOfCard=typeOfCard
        self.issuedDate=issuedDate
        self.expiryDate=expiryDate

    
