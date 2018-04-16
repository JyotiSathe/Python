import datetime
class Human(object):
    def __init__(self,name,gender,dob):
        print("In Human Constructor")
        self.name=name
        self.gender=gender
        self.dob=dob
    
class Employee(Human):
    def __init__(self,name,gender,dob,exp,salary,designation):
        Human.__init__(self,name,gender,dob)
        print("In Employee Contructor")
        self.exp=exp
        self.salary=salary
        self.designation=designation

def main():
    e1=Employee("Jyoti","F",datetime.date(1994,06,13),2,27000,"ASE")
    print e1.__dict__
    print type(e1.dob)

if __name__=='__main__':
    main()
