class EmployeeSalaryIncrement:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def increment(self,amount):
        def addToSalary():
            return self.salary+amount
        return addToSalary

def main():
    e1=EmployeeSalaryIncrement("jyoti",27000)
    e2=EmployeeSalaryIncrement("Max",30000)
    adder_3000=e1.increment(3000)

if __name__=='__main__':
    main()
