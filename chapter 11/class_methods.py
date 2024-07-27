class Employee:
    company = "Camel"
    salary = 100
    location = "Delhi"


    # def changeSalary(self, sal):
    #     self.__class__.salary = sal # always alternative for changing Class


    @classmethod
    def changeSalary(cls,sal):
        cls.salary = sal

e = Employee()
# print(e.salary)    
e.changeSalary(4550)
print(e.salary)
print(Employee.salary)