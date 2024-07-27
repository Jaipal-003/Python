class Person:
    country = "India"

    def __init__(self):
        print("Initializing Person..\n")
    
    def takeBreath(self):
       print("I am breathing...")    


class Employee(Person):
    company = "Honda"

    def __init__(self):
        super().__init__()
        print("Initializing Employee..\n")
    

    def getSalary (self):
        print(f"Salary os {self.getSalary}")

    def takeBreath(self):
        super().takeBreath()
        print("I am an Employee so I am  lickily breathing...")


class Programmer(Employee):
    company = "Fiverr"


    def __init__(self):
        super().__init__()
        print("Initializing Programmer..\n")    


    def getSalary(self):
        print(f"NO salary to Programmers")


    def takeBreath(self):
        super().takeBreath()
        print("I am an Employee so I am  lickily breathing+++ ...")    



# p = Person()
# p.takeBreath()



e = Employee()
# e.takeBreath()


 
pr = Programmer()
# pr.takeBreath()
 