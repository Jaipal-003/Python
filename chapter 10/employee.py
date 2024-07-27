class Employee:
    company = "Google"

harry = Employee()
rajni = Employee()
harry.salary =500
rajni.salary =600
print(harry.company)
print(rajni.company)
Employee.company = "Youtube"
print(harry.company)
print(rajni.company)
print(harry.salary)
print(rajni.salary)