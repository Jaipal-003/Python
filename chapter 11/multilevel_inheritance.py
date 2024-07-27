class Person:
    country = "India"

    def takeBreath(self):
       print("I am breathing...")    


class Employee(Person):
    company = "Honda"


    def getSalary (self):
        print(f"Salary os {self.getSalary}")

    def takeBreath(self):
        print("I am an Employee so I am  lickily breathing...")


class Programmer(Employee):
    company = "Fiverr"


    def getSalary(self):
        print(f"NO salary to Programmers")


    def takeBreath(self):
        print("I am an Employee so I am  lickily breathing+++ ...")    



p = Person()
p.takeBreath()
# print(p.company) # Throws an error


e = Employee()
e.takeBreath()
print(e.company)

 
pr = Programmer()
pr.takeBreath()
 