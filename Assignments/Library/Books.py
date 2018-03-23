class Books:
    Book_id=001
    
    def __init__(self,title,author,price,quantity,isAvailable="Y"):
        self.Book_id=Books.Book_id
        Books.Book_id+=1
        self.title=title
        self.author=author
        self.price=price
        self.quantity=quantity
        self.isAvailable=isAvailable

    def setQuantity(self,quantity):
        self.quantity=quantity
        
        
