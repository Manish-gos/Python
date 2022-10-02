n=int(input("Enter the number of employee"))
employees={}
for i in range(n):
    name=input("Enter employee name")
    salary=input("Enter employee salary")
    employees[name]=salary
while True:
    details=employees.get(input("Enter employee name for get salary details"),-1)
    if details== -1:
        print("Employee does not exist in data base")
    else:
        print("Employee salary is ",details)
    choice=input("Do you want other employee details yes/no")
    if choice=='no':
        break
