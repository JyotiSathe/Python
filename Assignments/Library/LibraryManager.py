from Books import Books
from Member import Member
from BookIssueHistory import BookIssueHistory

class LibraryManagerError(Exception):
    def __init__(self,message):
        self.message=message
    def __str__(self):
        return "Caught with an Exception:"+str(self.message)
    
class BookNotFoundException(LibraryManagerError):
    def __init__(self,book_id):
        LibraryManagerError.__init__(self,"Book is not present in library\n==========================")
        
class MemberNotFoundException(LibraryManagerError):
    def __init__(self,member_id):
        LibraryManagerError.__init__(self,"Member is not registered in library\n==========================")
        
class LibraryManager():
    Book_dict={}
    issuedBook_dict={}
    Members_dict={}
    
    def addMember(self,name,address,contactNo):
        obj=Member(name,address,contactNo)
        LibraryManager.Members_dict[obj.member_id]=obj
        print str(self.getMember(obj.member_id).member_id)+"\n"

    def updateMember(self,ch,criteria,member_id):
        try:
            obj=self.getMember(member_id)
            if(ch==1):
                obj.setAddress(criteria)
                print self.getMember(obj.member_id).address
            elif(ch==2):
                obj.setContactNumber(criteria)
                print self.getMember(obj.member_id).contactNo
        except MemberNotFoundException as e:
            print e
            
    def getMember(self,member_id):
        try:
            member=LibraryManager.Members_dict[member_id]
        except KeyError:
            raise MemberNotFoundException(member_id)
        return member 

    def removeMember(self,member_id):
        try:
            obj=self.getMember(member_id)
            LibraryManager.Members_dict.pop(member_id,"Member With {} is not present".format(member_id))
        except MemberNotFoundException as e:
            print e
            
    def addBook(self,title,author,price,quantity):
        book=Books(title,author,price,quantity)
        LibraryManager.Book_dict[book.Book_id]=book
        print self.getBook(book.Book_id).Book_id
        print

    def getBook(self,book_id):
        try:
            obj=LibraryManager.Book_dict[book_id]
        except KeyError:
            raise BookNotFoundException(book_id)
        return obj

    def updateQuantity(self,book_id,quantity):
        try:
            obj=self.getBook(book_id)
            obj.setQuantity(quantity)
            print self.getBook(obj.Book_id).quantity
        except BookNotFoundException as e:
            print e

    def checkIfAvailable(self,book_id):
        isAvailable=False
        try:
            obj=self.getBook(book_id)
            if(obj.isAvailable=="Y"):
                isAvailable=True
        except BookNotFoundException as e:
            print e
        return isAvailable

    def issueBook(self,member_id,book_id,numberOfDays):
        try:
            if(self.checkIfAvailable(book_id)):
                obj=self.getBook(book_id)
                member=self.getMember(member_id)
                LibraryManager.issuedBook_dict[member]=obj
                issueObj=BookIssueHistory("23-03-2018",obj.title,obj.author,numberOfDays)
                member.issuedHistory.append(issueObj)
                if(obj.quantity==1):
                    obj.quantity=0
                    obj.isAvailable="N"
                else:
                    obj.quantity-=1
                print self.getBook(obj.Book_id).quantity
            else:
                return "All Books are issued"
        except BookNotFoundException as e:
            print e
        except MemberNotFoundException as e:
            print e

    def returnBook(self,member_id,book_id):
        try:
            obj=self.getBook(book_id)
            member=self.getMember(member_id)
            obj.quantity+=1
            print self.getBook(obj.Book_id).quantity
            LibraryManager.issuedBook_dict.pop(member,"error")
        except BookNotFoundException as e:
            print e
        except MemberNotFoundException as e:
            print e

def Menu():
    print("Welcome To Library")
    print("1:Add Member\n2:Update Member Details\n3:Remove Member\n4:Add New Book\n5:Update Quantity Of Book:\n6:Check If Book Available\n7:Issue Book\n8:Return Book\n9:Exit")
    choice=input("Enter Your Choice")
    return choice
    
def main():
    choice=Menu()
    print
    lm=LibraryManager()
    while(choice<=8):
        if choice==1:
            print("Enter Member Details:")
            name=input("Enter Name:")
            address=input("Enter Address:")
            contactNo=input("Enter Contact Number")
            lm.addMember(name,address,contactNo)
        elif choice==2:
            print("1:Update Address\n2:Update Contact Number")
            ch=input("Enter Choice")
            member_id=input("Enter Member Id:")
            if ch==1:
                address=input("Enter New Address:")
                lm.updateMember(ch,address,member_id)
            elif ch==2:
                contactNo=input("Enter New Contact Number:")
                lm.updateMember(ch,contactNo,member_id)
            else:
                print("Invalid choice")
        elif choice==3:
            member_id=input("Enter Member Id:")
            lm.removeMember(member_id)
        elif choice==4:
            print("Add New Book")
            title=input("Enter Book Title:")
            author=input("Enter Author")
            price=input("Enter Price")
            quantity=input("Enter Quanity")
            lm.addBook(title,author,price,quantity)
        elif choice==5:
            book_id=input("Enter Book Id")
            quantity=input("Enter New Quantity")
            lm.updateQuantity(book_id,quantity)
        elif choice==6:
            book_id=input("Enter If Book Avaiable for Issue")
            if(lm.checkIfAvailable(book_id)):
                print ("Book Is Avaiable")
            else:
                print ("Book Not Available")
        elif choice==7:
            member_id=input("Enter Member Id")
            book_id=input("Enter Book To Be Issued")
            numberOfDays=input("Enter Number Of Days")
            lm.issueBook(member_id,book_id,numberOfDays)
        elif choice==8:
            member_id=input("Enter Member Id")
            book_id=input("Enter Book To Be Returned")
            lm.returnBook(member_id,book_id)
        else:
            return
        choice=Menu()
        print

if __name__=='__main__':
    main()
