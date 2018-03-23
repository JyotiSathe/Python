

class Member:
    member_id=1
    def __init__(self,name,address,contactNo):
        self.member_id=Member.member_id
        Member.member_id+=1
        self.name=name
        self.address=address
        self.contactNo=contactNo
        self.issuedHistory=[]

    def setAddress(self,address):
        self.address=address

    def setContactNumber(self,contactNo):
        self.contactNo=contactNo
