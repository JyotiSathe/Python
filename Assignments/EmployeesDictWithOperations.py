#WAP to accept employee details from user and perform following operations on it.
#1:create employees list
#2:search employee
#3:update details of employee
#4:display all employee
#5:insert an employee
#6:remove an employee
#details: name, date of birth, address and salary

def createEmployeesDict(employees_dict):
    no_of_employees=input("Enter number of employees")
    for i in range(no_of_employees):
        print("Enter Details for Employee: {}".format(i+1))
        name=input("Enter Name")
        dob=input("Enter Date of Birth In format dd-mm-yyyy")
        address=input("Enter Address")
        salary=input("Enter Salary")
        if(type(salary)==float and type(salary)!=str):
            employees_dict[i+1]={"Name":name,"DOB":dob,"Address":address,"Salary":salary}
        else:
            print("Salary should be in decimals and not string")
            salary=input("Enter Salary Again")
            employees_dict[i+1]={"Name":name,"DOB":dob,"Address":address,"Salary":salary}
            
def insertEmployee(employees_dict):
    if(len(employees_dict)==0):
        print("There is no employee list present, let's create!!")
        createEmployeesDict(employees_dict)
    else:
        name=input("Enter Name")
        dob=input("Enter Date of Birth In format dd-mm-yyyy")
        address=input("Enter Address")
        salary=input("Enter Salary")
        employees_dict[len(employees_dict)+1]={"Name":name,"DOB":dob,"Address":address,"Salary":salary}

def removeEmployee(employees_dict):
    flag=False
    if(len(employees_dict)==0):
        flag=False
    else:
        eid=input("Enter employee id you want to remove")
        employee=employees_dict[eid]
        print "You are going to delete below employee"
        print("Employee id: {}".format(eid))
        print("Name: {}".format(employee["Name"]))
        print("DOB: {}".format(employee["DOB"]))
        print("Address: {}".format(employee["Address"]))
        print("Salary: {}".format(employee["Salary"]))
        ch=input("Do you want to continue?(y/n)")
        if(ch=='y'):
            employees_dict.pop(eid)
            flag=True
        elif(ch=='n'):
            print("Remove Action is Aborted")
        else:
            print("You have not enetered valid choice")
    return flag

def updateEmployeeDetails(employees_dict):
    flag=False
    if(len(employees_dict)==0):
        flag=False
    else:
        eid=input("Enter employee id whose details you want to update")
        choice=input("What you want to update 1:Address or 2:Salary? (1/2)")
        if(choice==1):
            employee=employees_dict[eid]["Address"]=input("Enter new address")
            flag=True
        elif(choice==2):
            employee=employees_dict[eid]["Salary"]=input("Enter new salary")
            flag=True
        else:
            print("Please enter valid choice")
            updateEmployeeDetails(employees_dict)
    return flag

def searchEmployee(employees_dict):
    result=""
    if(len(employees_dict)==0):
        result="There is no employee list"
    else:
        eid=input("Enter employee id whom you want to search")
        if(employees_dict.has_key(eid)):
            result+="Employee is present, below are details\n"
            result+="Name: {}".format(employees_dict[eid]["Name"])
            result+="\nDOB: {}".format(employees_dict[eid]["DOB"])
            result+="\nAddress: {}".format(employees_dict[eid]["Address"])
            result+="Salary: {}".format(employees_dict[eid]["Salary"])
        else:
            result="Employee with id {} is not present".format(eid)
    return result
        
def printEmployees(employees_dict):
    if(len(employees_dict)==0):
        print("There is no employee present")
    else:
        for key in employees_dict:
            print("Employee Id: {}".format(key))
            print("Name: {}".format(employees_dict[key]["Name"]))
            print("DOB: {}".format(employees_dict[key]["DOB"]))
            print("Address: {}".format(employees_dict[key]["Address"]))
            print("Salary: {}".format(employees_dict[key]["Salary"]))
            print("")

def go_to_choice(choice,employees_dict):
    if choice==1:
        createEmployeesDict(employees_dict)
        return "List of employees created"
    elif choice==2:
        insertEmployee(employees_dict)
        return "Employee is added in list"
    elif choice==3:
        printEmployees(employees_dict)
        return ""
    elif choice==4:
        result=removeEmployee(employees_dict)
        if(not result):
            return "There is no employee present"
        else:    
            return "Employee is removed successfully"
    elif choice==5:
        result=updateEmployeeDetails(employees_dict)
        if(not result):
            return "There is no employee present"
        else:    
            return "Employee Details are updated successfully"
    elif choice==6:
        result=searchEmployee(employees_dict)
        return result
    else:
        return

def Menu():
    print("*******************")
    print("Employee Management")
    print("1: Create Employee List")
    print("2: Insert An Employee in existing list")
    print("3: Display all Employees")
    print("4: Remove Employee")
    print("5: Update Employee Details")
    print("6: Search For Employee")
    print("7: Exit")
    choice=input("Enter your choice")
    print("*******************")
    return choice

def main():
    employees_dict={}
    choice=Menu()
    result=go_to_choice(choice,employees_dict)
    while(result!=None):
        print result
        choice=Menu()
        result=go_to_choice(choice,employees_dict)
        
if __name__=='__main__':
    main()
