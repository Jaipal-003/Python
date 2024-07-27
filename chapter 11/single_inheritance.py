class Employee:
    company = "Google"

    def showDatials(self):
        print("This is an employee")


class Programmer(Employee):
    language = "Python"


    def getLanguage(self):
        print(f"The language is {self.language}")


    def showDatials(self):
        print("This is an programmer")     


e = Employee()
e.showDatials()
p = Programmer()
p.showDatials()
p.getLanguage()


